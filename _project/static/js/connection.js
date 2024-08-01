const zwraper = document.querySelector('.zwraper'),
toast = zwraper.querySelector('.toast'),
title = toast.querySelector('span'),
subtitle = toast.querySelector('p'),
wifiIcon = toast.querySelector('.icon');

function setStatus(status){
    console.log(status?'online':'offline')
}
setStatus(navigator.status)
window.addEventListener('online',e =>{
    setStatus(true)
    zwraper.classList.remove('hide');
    toast.classList.remove('offline');
    title.innerText = 'you are online now';
    subtitle.innerText='Your internet connection is working perfectly'
    wifiIcon.innerHTML = '<i class="fa-solid fa-wifi"></i>'
    setTimeout(()=>{
        zwraper.classList.add('hide');
    },5000);
})
setStatus(navigator.status)
window.addEventListener('offline',e =>{
    setStatus(false)
    zwraper.classList.remove('hide');
        toast.classList.add('offline');
        title.innerText = 'you are offline now';
        subtitle.innerText='Check your internet connection and try again later';
        wifiIcon.innerHTML = '<i class="fa-solid fa-signal-off"></i>';
        setTimeout(()=>{
            zwraper.classList.add('hide');
        },5000);
})
    // function ajax(){
    //     let xhr = new XMLHttpRequest();
    //     xhr.open("GET", "https://jsonplaceholder.typicode.com/posts",true);
    //     xhr.onload=()=>{
    //         if(xhr.status==200 &&  xhr.status <300){
    //             toast.classList.remove('offline');
    //             title.innerText = 'you are online now';
    //             subtitle.innerText='Your internet connection is working perfectly'
    //             wifiIcon.innerHTML = '<i class="fa-solid fa-wifi"></i>'
    //             setTimeout(()=>{
    //                 zwraper.classList.add('hide');
    //             },3000);
    //         }else{
    //             offline();
    //         }
    //     }
    //     xhr.onerror =()=>{
    //         offline();
    //     }
    //     xhr.send();
    // }
    // function offline(){
    //     zwraper.classList.remove('hide');
    //     toast.classList.add('offline');
    //     title.innerText = 'you are offline now';
    //     subtitle.innerText='Check your internet connection and try again later';
    //     wifiIcon.innerHTML = '<i class="fa-solid fa-signal-off"></i>';
    // }
    // setInterval(()=>{
    //     ajax();
    // },1000);