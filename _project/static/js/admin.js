//defining html elements
const sellsdel = document.querySelectorAll('#sellsdel')
const sellsup = document.querySelectorAll('#sellsup')
const daycome = document.getElementById('daycome')
const monthcome = document.getElementById('monthcome')
// const loses = document.getElementById('loses')
const windowcon = document.getElementById('windowcon')
const closedetwin = document.getElementById('closedetwin')
const rightconexpend = document.getElementById('rightconexpend')
const rightcon = document.querySelector('.rightcon')
let income = document.getElementById('income').innerText
let loseing = document.getElementById('loseing').innerText
let todaydate = document.getElementById('todaydate')
//-----------------------------------------------------------------------------------------------------------
// Get all date input elements
const dateInputs = document.querySelectorAll('input[type="date"]');
// Get today's date
const today = new Date();
todaydate.textContent = today.toISOString().split('T')[0];
// Loop through each input and set its value to today's date
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
daycome.onclick=()=>{
    const metadata = daycome.getAttribute('metadata')
    windowcon.style.visibility = 'visible'
    windowcon.style.opacity = '1'
    document.getElementById('detailcontainer').innerHTML=metadata
    
}
monthcome.onclick=()=>{
    const metadata = monthcome.getAttribute('metadata')
    windowcon.style.visibility = 'visible'
    windowcon.style.opacity = '1'
    document.getElementById('detailcontainer').innerHTML=metadata
    
}
// loses.onclick=()=>{
//     const metadata = loses.getAttribute('metadata')
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
    document.getElementById('remain').innerText = parseFloat(income-loseing)
}
//-----------------------------------------------------------------------------------------------------------
