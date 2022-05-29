from venv import create
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .serializers import PostSerializer
from .models import Post

POSTS_URL = reverse('post:post-list')

def detail_url(post_id):
      return reverse('post:post-detail', args=[post_id])

def create_post():
      return Post.objects.create(title="Test Title", body="Test Body Test Body")

class TestPosts(TestCase):
      """Tests everything related to Posts"""

      def setUp(self):
            self.client = APIClient()


      def test_list_all_posts(self):
            """Tests that all posts in the database are showing."""
            post1 = Post.objects.create(title="Test post1", body="This is a test post, the first of three.")
            post2 = Post.objects.create(title="Test post2", body="This is a test post, the second of three.")
            post3 = Post.objects.create(title="Test post3", body="This is a test post, the third of three.")

            res = self.client.get(POSTS_URL)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(len(res.data), 3)

      
      def test_create_post(self):
            post = create_post()
            res = self.client.get(POSTS_URL)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data[0]['title'], post.title)
      
      
      def test_retrieve_post_detail(self):
            """Tests that post detail is retrieved"""
            post = create_post()
            url = detail_url(post.id)

            res = self.client.get(url)
            serializer = PostSerializer(post)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, serializer.data)

      
      def test_update_post(self):
            """Tests that posts are updated"""
            post = create_post()

            payload = {
                  "title": "Updated Title"
            }
            
            url = detail_url(post.id)

            res = self.client.patch(url, payload)

            post.refresh_from_db()

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data['title'], payload['title'])

      
      def test_delete_post(self):
            """Tests that the post is destroyed like the rest of us."""
            post = create_post()
            url = detail_url(post.id)

            res = self.client.delete(url)

            self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(res.data, None)