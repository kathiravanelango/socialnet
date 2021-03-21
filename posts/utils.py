# Utility functions
def serializeOnePost(post):
	data = {
		"author": {
            'username':post.author.username,
            'image':post.author.profile.image.url
        },
		"image": post.image.url,
		"caption": post.caption
	}
	return data

def serializeManyPosts(posts):
	results = []
	for post in posts:
		results.append(serializeOnePost(post))
	return results