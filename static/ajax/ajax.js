function like(slug , id){
    var heart = document.getElementById('like')
    var count = document.getElementById('count')
    $.get(`/post/like/${slug}/${id}`).then(response =>{
        if (response['response'] === 'liked') {
            heart.className = 'fa fa-heart'
            count.innerText = Number(count.innerText) + 1
        }
        else{
            heart.className = 'fa fa-heart-o'
            count.innerText = Number(count.innerText) - 1

        }
    })
}