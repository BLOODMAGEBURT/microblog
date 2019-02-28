from rq import get_current_job
import sys
import json
from flask import render_template
from app import create_app
from app import db
from app.models import Task, User, Post
from app.email import send_email

app = create_app()
app.app_context().push()


def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()

        task = Task.query.filter_by(id=job.get_id()).first()
        task.user.add_notification('task_progress', {'task_id': job.get_id(), 'progress': progress})

        if progress >= 100:
            task.complete = True
        db.session.commit()


def export_posts(user_id):
    try:
        # read user posts from database
        user = User.query.get(user_id)
        _set_task_progress(0)

        total_count = user.posts.count()
        data = []
        i = 0
        for post in user.posts.order_by(Post.timestamp.asc()):
            data.append({'body': post.body, 'timestamp': post.timestamp.isoformat() + 'Z'})
            i += 1
            _set_task_progress(100 * i / total_count)

        # send email with data to user
        send_email('[Microblog] Your blog posts',
                   sender=app.config['MAIL_USERNAME'],
                   recipients=[user.email],
                   text_body=render_template('email/export_posts.txt', user=user),
                   html_body=render_template('email/export_posts.html', user=user),
                   attachments=[('posts.json', 'application/json', json.dumps({'posts': data}, indent=4))],
                   sync=True
                   )
    except:
        # handle unexpected errors: rq errors
        _set_task_progress(100)
        app.logger.error('Unhandled exception', exc_info=sys.exc_info)
