document.addEventListener("DOMContentLoaded", function(){
    const back=document.getElementById('myBox');
    const bob=document.createElement('div');
    const backWidth=400;
    const backHeight=600;
    const bobWidth=60;
    const bobHeight=85;
    const numBoards=5;
    const boardSpeed=4;
    const FPS=30;
    const gravity=1; //Yeah, flerfleas! I invented gravity, it exists!
    let boards=[];
    let score=0;
    let GameOVer=false;
    let bobStartX=50;
    let bobStartY=150;
    let bobBottomSpace=bobStartY;


    function createBob(){
        back.appendChild(bob);
        bob.classList.add('bob');
        bob.style.left=bobStartX+'px';
        bob.style.bottom=bobStartY+'px';
    }

    class board {
        constructor(newBoardBottom){
            this.visual=document.createElement('div');
            this.left=Math.random()*(backWidth-bobWidth);
            this.bottom=newBoardBottom;
            const b=this.visual;
            b.classList.add('board');
            b.style.left=this.left+'px';
            b.style.bottom=this.bottom+'px';
            back.appendChild(b);
        }
    }
    function createBoards(){
        for(vdo=0;vdo<numBoards;vdo++){
            let boardGap=backHeight/numBoards;
            let newBoardBottom=100+(vdo*boardGap)
            let newBoard= new board(newBoardBottom);
            boards.push(newBoard);
        }
    }

    function main(){
        if(!GameOVer){
            createBoards();
            createBob();  
        }else{
            
        }

    }
    main();
})

