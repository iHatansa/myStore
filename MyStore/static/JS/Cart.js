var updateBtns = document.getElementsByClassName('btn');


for (i = 0; i < updateBtns.length; i++) {
updateBtns[i].addEventListener('click', function(){
  var productId = this.dataset.product
  var action = this.dataset.action
  var SessionId = this.dataset.id
  console.log('productId:', productId, 'Action:', action)
  updateUserOrder(productId, action)
		
  
})
}



function updateUserOrder(productId, action){
	
	
		var url = '/store/UpdateItem/'

		fetch(url,{
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		   location.reload()
           console.log('data', data);
		});
}






