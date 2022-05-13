const like = (postId) => {
    const likeCount = document.getElementById(`likes-count-${postId}`)
    const likesButton = document.getElementById(`like-button-${postId}`)

    fetch(`/like_post/${postId}`,{method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            likeCount.innerHTML = data['likes']

            if(data['liked'] === true){
                likesButton.className = 'fas fa-thumbs-up'
            }

            else{
                likesButton.className = 'far fa-thumbs-up'
            }
        })
        .catch((e) => alert('Could not like post'))

    
}