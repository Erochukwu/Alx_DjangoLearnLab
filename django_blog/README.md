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
