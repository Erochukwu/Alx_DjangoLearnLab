# Django Blog App

## Overview
The **Blog app** allows users to **create, read, update, and delete (CRUD)** blog posts.  
User authentication ensures that only authors can edit or delete their own posts.

---

## Models

**Post**
- `title` (CharField) – Post title
- `content` (TextField) – Main content
- `date_posted` (DateTimeField) – Automatically set on creation
- `author` (ForeignKey to User) – Creator of the post

**Methods**
- `__str__()` – Returns post title
- `get_absolute_url()` – Returns URL for post detail view

---

## Forms

**PostForm**
- Fields: `title`, `content`
- Validation: Ensures fields are not empty
- Used for both creating and editing posts

---

## Views

| View | Description | Access |
|------|------------|-------|
| `PostListView` | Lists all posts (paginated, newest first) | Everyone |
| `PostDetailView` | Shows full content of a single post | Everyone |
| `PostCreateView` | Create a new post | Authenticated users |
| `PostUpdateView` | Edit an existing post | Post author only |
| `PostDeleteView` | Delete a post | Post author only |

**Mixins**
- `LoginRequiredMixin` – Restricts create/edit/delete to logged-in users
- `UserPassesTestMixin` – Ensures only authors can modify their posts

---

## URLs

| URL | View | Name |
|-----|------|------|
| `/` or `/posts/` | `PostListView` | `post_list` / `posts` |
| `/post/<int:pk>/` | `PostDetailView` | `post_detail` |
| `/post/new/` | `PostCreateView` | `post_create` |
| `/post/<int:pk>/edit/` | `PostUpdateView` | `post_update` |
| `/post/<int:pk>/delete/` | `PostDeleteView` | `post_delete` |

---

## Templates

- `post_list.html` – Displays all posts with pagination
- `post_detail.html` – Shows a single post; Edit/Delete links only for the author
- `post_form.html` – For creating/editing posts
- `post_confirm_delete.html` – Confirmation page for deletion

**Example permission check:**
```django
{% if user.is_authenticated and post.author == user %}
    <a href="{% url 'post_update' post.pk %}">Edit</a>
    <a href="{% url 'post_delete' post.pk %}">Delete</a>
{% endif %}


Comment System Documentation
Overview

The Comment System allows users to interact with blog posts by leaving feedback in the form of comments. It supports creating, editing, and deleting comments, with rules that ensure only the rightful author can manage their own comments.

Features

Users can:

Add comments to posts.

Edit their own comments.

Delete their own comments.

Visitors (unauthenticated users) can:

View comments but cannot create, edit, or delete them.

Permissions:

Only the comment author (or an admin) can edit or delete a comment.

Comments are displayed under each post in reverse chronological order.

Code Components
Models

Comment model stores:

post → Linked to a specific blog post.

author → The user who wrote the comment.

content → The body of the comment.

created_at / updated_at → Timestamps for tracking comment activity.

Forms

CommentForm provides a simple text area for users to submit or edit their comments.

Views

CommentCreateView → Allows logged-in users to add a new comment under a post.

CommentUpdateView → Restricts editing to the comment’s author only.

CommentDeleteView → Restricts deletion to the comment’s author only.

URLs

/post/<post_id>/comment/new/ → Create a comment on a specific post.

/comment/<comment_id>/edit/ → Edit a comment.

/comment/<comment_id>/delete/ → Delete a comment.

Templates
Post Detail Page (post_detail.html)

Displays all comments under a post.

Shows Edit and Delete links only to the comment’s author.

Provides a comment form for logged-in users.

Prompts guests to log in before commenting.

Delete Confirmation Page (comment_confirm_delete.html)

Confirms before permanently deleting a comment.

### Usage Guide

Adding a Comment

Open a post’s detail page.

Scroll to the comment section.

Logged-in users can type and submit a comment form.

Editing a Comment

Click the Edit link under your comment.

Update the text and save changes.

Deleting a Comment

Click the Delete link under your comment.

Confirm deletion to remove it permanently.

### Tagging System
How it works

Each post can have one or more tags.

Tags help organize content and make it easier for users to find related posts.

How to add tags

When creating or editing a post, use the tags field.

Enter tags as a comma-separated list (e.g., django, blog, tutorial).

Tags will automatically be saved and linked to the post.

Viewing tags

Tags are displayed below each post.

Clicking on a tag will show all posts associated with that tag at /tags/<tag_name>/.

Search Functionality
How it works

Users can search posts by typing keywords in the search bar.

The search will look through:

Post titles

Post content

Post tags

Usage

Enter a keyword (e.g., django) in the search bar.

Matching posts will be displayed on the Search Results page.

The search results page is available at /search/?q=your_keyword.

URL Configuration

Key URL patterns:

/ → Post list

/post/<id>/ → Post details

/tags/<tag_name>/ → Filter posts by tag

/search/?q=<query> → Search posts by keyword
The project includes tests for tagging and search. Run them with:
python manage.py test blog.tests


Tech Stack

Python 3.12+

Django 5.x

PostgreSQL / SQLite (default: SQLite)

django-taggit