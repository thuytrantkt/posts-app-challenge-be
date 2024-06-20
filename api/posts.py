from flask import Blueprint, jsonify, Response, request
from models import Post, Comment, db
from flask_cors import CORS,cross_origin

posts = Blueprint("posts", __name__)


@posts.route("/posts", methods=["GET"])
@cross_origin()
def get_posts() -> Response:
    posts: list[Post] = Post.query.all()

    comment_counts: list[tuple[int, int]] = (
        db.session.query(Comment.post_id, db.func.count(Comment.id))
        .group_by(Comment.post_id)
        .all()
    )

    comment_counts_dict = {post_id: count for post_id, count in comment_counts}

    return jsonify(
        [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username,
                "createdAt": post.created_at,
                "commentCount": comment_counts_dict.get(post.id, 0),
            }
            for post in posts
        ]
    )


@posts.route("/posts/<int:id>/comments", methods=["GET"])
@cross_origin()
def get_comments(id: int) -> Response:
    page_number: int = int(request.args.get("page", default=1))
    per_page: int = int(request.args.get("per-page", default=1))

    comments = (
        Comment.query.filter_by(post_id=id)
        .limit(per_page)
        .offset((page_number - 1) * per_page)
        .all()
    )

    return jsonify(
        [
            {
                "id": comment.id,
                "content": comment.content,
                "author": comment.author.username,
                "createdAt": comment.created_at,
            }
            for comment in comments
        ]
    )
