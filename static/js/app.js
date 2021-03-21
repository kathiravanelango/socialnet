const postsContainer = document.querySelector('.infinite-container')
const loadMoreBtn = document.querySelector('#loadMore')

let pageNum = 2
let hasMore = true

function renderPosts(posts) {
    posts.forEach(post => {
        const postDiv = document.createElement('div')
        postDiv.classList.add('post-container')
        postDiv.classList.add('mt-4')
        postDiv.classList.add('infinite-item')
        postDiv.innerHTML = `
            <div class="post-header">
                <div class="post-user-image">
                    <img width="40" height="40" style="object-fit: cover;" class="rounded-circle ml-1"
                        src="${post.author.image}" alt="">
                </div>
                <div class="post-author">
                    <h6><a href="/${post.author.username}">${post.author.username}</a></h6>
                </div>
            </div>
            <div class="post-image">
                <img src="${post.image}" alt="">
            </div>
            <div class="post-caption">
                <p>${post.caption}</p>
            </div>`

        postsContainer.appendChild(postDiv)
    });
}

async function getNextPosts() {
    if (!hasMore) return

    try {
        const response = await fetch(`/post/getmore?page_num=${pageNum}`)
        const { posts, has_more, next_page, report } = await response.json()

        if (!report) return

        hasMore = has_more
        if (hasMore)
            pageNum = next_page
        else
            loadMoreBtn.disabled = true

        renderPosts(posts)
    }
    catch (error) {
        console.error(error)
    }
}

loadMoreBtn.addEventListener('click', getNextPosts)