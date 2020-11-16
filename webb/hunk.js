document.addEventListener("DOMContedLoaded", function(){
    const box = document.querySelector(".main");
    const plupp=document.querySelector(".plupp");
    const mainWidth=600;
    const mainHeight=600;
    const pluppSize=50;

    function init(){
        plupp.style.top=((mainHeight/2)-(pluppSixe/2))+'px';
        plupp.style.left=((mainWidth/2)-(pluppSixe/2))+'px';

    }

    function main(){
        init();


    }
    main();

});
