document.addEventListener('DOMContentLoaded', function() {
    var likeButton = document.getElementById('like-button');
    likeButton.addEventListener('click', function() {
        var postId = this.getAttribute('data-post-id');
        fetch(`/like/${postId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
                'Content-Type': 'application/json'
            },
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            if (data.liked !== undefined) {
                likeButton.innerText = data.liked ? 'Unlike' : 'Like';
                document.getElementById('likes-count').innerText = data.likes_count;
            }
        });
    });
});