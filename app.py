import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Snake Bello Chico VIP", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #1a1a2e;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #f1c40f; font-family: sans-serif; text-shadow: 2px 2px #3498db;'>🐍 Snake Bello Chico</h1>", unsafe_allow_html=True)

game_code = """
<div id="game-container" style="position:relative; text-align:center; font-family: sans-serif; background: #1a1a2e; padding: 15px; border-radius: 20px;">
    
    <div id="game-over-screen" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(255, 0, 0, 0.9); z-index:10; border-radius:20px; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:white; font-size:40px; text-shadow: 0 0 20px black;">BOOM !</h1>
        <p style="color:white; font-size:24px; font-weight:bold; margin-bottom:20px;">Khrat 3lik papaya !</p>
        <button onpointerdown="location.reload()" style="padding:15px 30px; font-size:20px; background:white; color:red; border:none; border-radius:50px; font-weight:bold; cursor:pointer;">REESSAYER 🔄</button>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <div style="font-size:22px; color:#f1c40f; font-weight:bold;">Mika K7la : <span id="score" style="color:white;">0</span></div>
        <div style="font-size:16px; color:#00d2ff; font-weight:bold; border:1px solid #00d2ff; padding:2px 8px; border-radius:8px;">Mode: Minion</div>
    </div>
    
    <canvas id="snakeGame" tabindex="0" style="border:4px solid #3498db; border-radius:15px; background:#24344d; touch-action:none; width: 95%; max-width: 350px; aspect-ratio: 1/1; outline: none;"></canvas>
    
    <div style="margin-top:20px; display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; width:210px; margin-left:auto; margin-right:auto;">
        <div></div>
        <button onpointerdown="changeDir('UP'); event.preventDefault();" style="height:65px; border-radius:18px; background:#3498db; color:white; border:none; font-size:26px; box-shadow: 0 4px #2980b9; cursor:pointer; touch-action: manipulation;">⬆️</button>
        <div></div>
        <button onpointerdown="changeDir('LEFT'); event.preventDefault();" style="height:65px; border-radius:18px; background:#3498db; color:white; border:none; font-size:26px; box-shadow: 0 4px #2980b9; cursor:pointer; touch-action: manipulation;">⬅️</button>
        <button onpointerdown="changeDir('DOWN'); event.preventDefault();" style="height:65px; border-radius:18px; background:#3498db; color:white; border:none; font-size:26px; box-shadow: 0 4px #2980b9; cursor:pointer; touch-action: manipulation;">⬇️</button>
        <button onpointerdown="changeDir('RIGHT'); event.preventDefault();" style="height:65px; border-radius:18px; background:#3498db; color:white; border:none; font-size:26px; box-shadow: 0 4px #2980b9; cursor:pointer; touch-action: manipulation;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");
    canvas.width = 400; canvas.height = 400;
    const box = 20;
    
    let score = 0;
    let snake = [{x: 10 * box, y: 10 * box}, {x: 9 * box, y: 10 * box}];
    let food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
    let d = "RIGHT";
    let changingDirection = false;
    let gameLoop; 

    canvas.focus();

    canvas.addEventListener("keydown", function(event) {
        if([37, 38, 39, 40].indexOf(event.keyCode) > -1) {
            event.preventDefault(); 
        }
        if(event.keyCode == 37) changeDir("LEFT");
        if(event.keyCode == 38) changeDir("UP");
        if(event.keyCode == 39) changeDir("RIGHT");
        if(event.keyCode == 40) changeDir("DOWN");
    });

    function changeDir(dir) {
        if (changingDirection) return;

        let directionChanged = false;

        if(dir == "UP" && d != "DOWN" && d != "UP") { d = "UP"; directionChanged = true; }
        if(dir == "DOWN" && d != "UP" && d != "DOWN") { d = "DOWN"; directionChanged = true; }
        if(dir == "LEFT" && d != "RIGHT" && d != "LEFT") { d = "LEFT"; directionChanged = true; }
        if(dir == "RIGHT" && d != "LEFT" && d != "RIGHT") { d = "RIGHT"; directionChanged = true; }

        if (directionChanged) {
            changingDirection = true;
            clearInterval(gameLoop);
            draw(); 
            gameLoop = setInterval(draw, 150);
        }
    }

    function drawMinionSegment(x, y, isHead) {
        ctx.fillStyle = "#f1c40f";
        ctx.beginPath();
        ctx.roundRect(x + 1, y + 1, box - 2, box - 2, 8);
        ctx.fill();

        ctx.fillStyle = "#3498db";
        ctx.fillRect(x + 1, y + 12, box - 2, 7);

        if(isHead) {
            ctx.fillStyle = "#333";
            ctx.fillRect(x + 1, y + 6, box - 2, 4);
            ctx.fillStyle = "white";
            ctx.beginPath(); ctx.arc(x + 10, y + 8, 5, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "#795548"; 
            ctx.beginPath(); ctx.arc(x + 10, y + 8, 2, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "black"; 
            ctx.beginPath(); ctx.arc(x + 10, y + 8, 1, 0, Math.PI * 2); ctx.fill();
        }
    }

    function drawMika(x, y) {
        ctx.shadowBlur = 15; ctx.shadowColor = "white";
        ctx.fillStyle = "#000000";
        ctx.beginPath(); ctx.roundRect(x + 3, y + 5, 14, 12, 3); ctx.fill();
        ctx.beginPath(); ctx.moveTo(x+10, y+5); ctx.lineTo(x+5, y+1); ctx.lineTo(x+15, y+1); ctx.fill();
        ctx.shadowBlur = 0;
    }

    function draw() {
        changingDirection = false; 

        ctx.fillStyle = "#24344d"; 
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let i = 0; i < snake.length; i++) {
            drawMinionSegment(snake[i].x, snake[i].y, i === 0);
        }

        drawMika(food.x, food.y);

        let snakeX = snake[0].x;
        let snakeY = snake[0].y;
        if( d == "LEFT") snakeX -= box;
        if( d == "UP") snakeY -= box;
        if( d == "RIGHT") snakeX += box;
        if( d == "DOWN") snakeY += box;

        if(snakeX == food.x && snakeY == food.y) {
            score++;
            scoreElement.innerHTML = score;
            food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
        } else {
            snake.pop();
        }

        let newHead = {x: snakeX, y: snakeY};
        if(snakeX < 0 || snakeX >= canvas.width || snakeY < 0 || snakeY >= canvas.height || collision(newHead, snake)) {
            clearInterval(gameLoop);
            document.getElementById("game-over-screen").style.display = "flex";
            return;
        }
        snake.unshift(newHead);
    }

    function collision(head, array) {
        for(let i = 0; i < array.length; i++) {
            if(head.x == array[i].x && head.y == array[i].y) return true;
        }
        return false;
    }

    gameLoop = setInterval(draw, 150);
</script>
"""

components.html(game_code, height=900)
