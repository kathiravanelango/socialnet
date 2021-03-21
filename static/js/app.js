const postsContainer = document.querySelector('.infinite-container')
const nextPostBtn = document.querySelector('#loadMore')

async function getNextPosts() {
    const response = await fetch('/post/getmore')
    const data = await response.json()
    console.log(data)
}

nextPostBtn.addEventListener('click', getNextPosts)