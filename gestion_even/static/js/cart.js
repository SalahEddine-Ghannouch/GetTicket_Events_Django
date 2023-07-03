var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var eventId = this.dataset.event
        var action = this.dataset.action
        console.log('event id : ', eventId, 'action :',action)
        console.log(' User : ', user)
        if(user == 'AnonymousUser'){
            console.log(' User Not logged ')
        }
        else{
            console.log(' User logged ')
        }
    })
}