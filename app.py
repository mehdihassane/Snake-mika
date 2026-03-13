import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page pour mobile
st.set_page_config(page_title="Snake Bello Chico", layout="centered")

# Style pour masquer l'interface Streamlit et épurer le look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #1a1a2e;}
    </style>
    """, unsafe_allow_html=True)

# Titre du jeu personnalisé
st.markdown("<h1 style='text-align: center; color: #00d2ff; font-family: sans-serif; text-shadow: 2px 2px #f1c40f;'>🐍 Snake Bello Chico</h1>", unsafe_allow_html=True)

game_code = """
<div id="game-container" style="position:relative; text-align:center; font-family: 'Segoe UI', sans-serif; background: #1a1a2e; padding: 15px; border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.5);">
    
    <div id="game-over-screen" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(26, 26, 46, 0.9); z-index:10; border-radius:20px; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:#ff4b2b; font-size:40px; text-shadow: 0 0 20px #ff4b2b; margin-bottom:10px;">GAME OVER</h1>
        <p style="color:#ffffff; font-size:24px; font-weight:bold; margin-bottom:20px;">Khrat 3lik papaya !</p>
        <button onclick="location.reload()" style="padding:15px 30px; font-size:20px; background:#2ecc71; color:white; border:none; border-radius:50px; box-shadow: 0 5px #27ae60; cursor:pointer;">REJOUER 🔄</button>
    </div>

    <div style="font-size:28px; color:#f1c40f; font-weight:bold; margin-bottom:15px; text-shadow: 0 0 8px rgba(241, 196, 15, 0.5);">
        Mika Ke7la : <span id="score" style="color:#ffffff;">0</span>
    </div>
    
    <canvas id="snakeGame" style="border:4px solid #f1c40f; border-radius:15px; background:#24344d; touch-action:none; width: 95%; max-width: 350px; aspect-ratio: 1/1; box-shadow: 0 0 15px rgba(241, 196, 15, 0.2);"></canvas>
    
    <div id="ui-controls" style="margin-top:25px; display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; width:220px; margin-left:auto; margin-right:auto;">
        <div></div>
        <button onclick="changeDir('UP')" style="height:70px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px; box-shadow: 0 4px #000;">⬆️</button>
        <div></div>
        
        <button onclick="changeDir('LEFT')" style="height:70px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px; box-shadow: 0 4px #000;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="height:70px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px; box-shadow: 0 4px #000;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="height:70px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px; box-shadow: 0 4px #000;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const gameOverScreen = document.getElementById("game-over-screen");
    canvas.width = 400;
    canvas.height = 400;
    
    const scoreElement = document.getElementById("score");
    const box = 20;
    let score = 0;
    let snake = [{x: 10 * box, y: 10 * box}, {x: 9 * box, y: 10 * box}];
    let food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
    let d = "RIGHT";

    function changeDir(dir) {
        if(dir == "UP" && d != "DOWN") d = "UP";
        if(dir == "DOWN" && d != "UP") d = "DOWN";
        if(dir == "LEFT" && d != "RIGHT") d = "LEFT";
        if(dir == "RIGHT" && d != "LEFT") d = "RIGHT";
    }

    function drawMika(x, y) {
        ctx.shadowBlur = 15;
        ctx.shadowColor = "rgba(255, 255, 255, 0.8)";
        ctx.fillStyle = "#000000";
        ctx.beginPath();
        ctx.roundRect(x + 3, y + 5, 14, 12, 3);
        ctx.fill();
        ctx.beginPath();
        ctx.moveTo(x+10, y+5); ctx.lineTo(x+5, y+1); ctx.lineTo(x+15, y+1); ctx.fill();
        ctx.shadowBlur = 0;
    }

    function draw() {
        ctx.fillStyle = "#24344d"; 
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let i = 0; i < snake.length; i++) {
            ctx.fillStyle = (i == 0) ? "#2ecc71" : "#27ae60";
            ctx.beginPath();
            ctx.roundRect(snake[i].x + 1, snake[i].y + 1, box - 2, box - 2, i == 0 ? 8 : 4);
            ctx.fill();
            
            if(i == 0) {
                ctx.fillStyle = "white";
                ctx.beginPath(); ctx.arc(snake[i].x + 6, snake[i].y + 7, 3, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 14, snake[i].y + 7, 3, 0, 2*Math.PI); ctx.fill();
                ctx.fillStyle = "black";
                ctx.beginPath(); ctx.arc(snake[i].x + 6, snake[i].y + 7, 1, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 14, snake[i].y + 7, 1, 0, 2*Math.PI); ctx.fill();
            }
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
            clearInterval(gameInterval);
            // ON AFFICHE L'ECRAN DE MORT EN COULEURS
            gameOverScreen.style.display = "flex";
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

    let gameInterval = setInterval(draw, 150);
</script>
"""

components.html(game_code, height=850)
