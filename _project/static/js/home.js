//defining html elements
const sellsdel = document.querySelectorAll('#sellsdel')
const sellsup = document.querySelectorAll('#sellsup')
const windowcon = document.getElementById('windowcon')
const closedetwin = document.getElementById('closedetwin')
// const losesbtn = document.getElementById('losesbtn')
const rightconexpend = document.getElementById('rightconexpend')
const rightcon = document.querySelector('.rightcon')
let todaydate = document.getElementById('todaydate')
let price = document.getElementById('price');
let papers = document.getElementById('papers');
let copies = document.getElementById('copies');
let total = document.getElementById('total');
let paid = document.getElementById('paid');
let remaining = document.getElementById('remaining');
//-----------------------------------------------------------------------------------------------------------
// Get all date input elements
const dateInputs = document.querySelectorAll('input[type="date"]');
// Get today's date
const today = new Date();
// Loop through each input and set its value to today's date
todaydate.textContent = today.toISOString().split('T')[0];
dateInputs.forEach(input => {
    input.value = today.toISOString().split('T')[0];
});
//-----------------------------------------------------------------------------------------------------------
//right container menu size funcion 
rightconexpend.addEventListener('click',()=>{
    rightcon.classList.toggle( "active" );
})
//-----------------------------------------------------------------------------------------------------------
//hidden window functions
// losesbtn.onclick=()=>{
//     const metadata = losesbtn.getAttribute('metadata')
//     windowcon.style.visibility = 'visible'
//     windowcon.style.opacity = '1'
//     document.getElementById('detailcontainer').innerHTML=metadata
    
// }
sellsdel.forEach((sellsdel)=>{
    sellsdel.onclick=()=>{
        const metadata = sellsdel.getAttribute('metadata')
        windowcon.style.visibility = 'visible'
        windowcon.style.opacity = '1'
        document.getElementById('detailcontainer').innerHTML=metadata
        
    }
})
sellsup.forEach((sellsup)=>{
    sellsup.onclick=()=>{
        const metadata = sellsup.getAttribute('metadata')
        windowcon.style.visibility = 'visible'
        windowcon.style.opacity = '1'
        document.getElementById('detailcontainer').innerHTML=metadata
    }
})
closedetwin.addEventListener('click',()=>{
    windowcon.style.top='0'
    windowcon.style.visibility='hidden'
    windowcon.style.opacity='0'
})
//-----------------------------------------------------------------------------------------------------------
//onload functions
window.onload=()=>{
    document.getElementById('search_bar').focus();
}
//-----------------------------------------------------------------------------------------------------------
//proccess functions ----------------------------------------------------------------------------------------
function geTotal(){
if(price.value !=''){
        const result = parseFloat(papers.value*copies.value*price.value);
        total.value = result;
        remaining.value =total.value;
    }else{
        total.value ='';
    }
};
price.addEventListener('keyup',()=>{
    geTotal();
});
paid.addEventListener('keyup',()=>{
    if(paid.value !=''){
        const result = parseFloat(total.value - paid.value);
        remaining.value = result;
    }else{
        remaining.value =total.value;
    }
});
//-----------------------------------------------------------------------------------------------------------
