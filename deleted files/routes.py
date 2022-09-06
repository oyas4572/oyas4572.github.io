from flask import render_template, url_for, flash, redirect, request, abort
from wb.spotify import playback
from wb.discordavatar import avatar
from wb.models import Post, User
from wb import app, database, bcrypt
import secrets
from flask_mail import Message

@app.route('/')
@app.route('/home')
def home():
    playbackdict = playback()
    page=request.args.get('page', 1, type=int)
    posts=Post.query.order_by(Post.date.desc()).paginate(per_page=5, page=page)

    return render_template('home.html', playback=playbackdict, avatar=avatar, posts=posts)

@app.route('/about')
def about():
    return render_template('home.html')


