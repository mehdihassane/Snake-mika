import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mika K7la Elite", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #1a1a2e;}
    </style>
    """, unsafe_allow_html=True)

game_code = """
<div id="game-container" style="text-align:center; font-family: sans-serif; background: #1a1a2e; padding: 15px; border-radius: 20px;">
    <div style="font-size:30px; color:#00d2ff; font-weight:bold; margin-bottom:10px; text-shadow: 0 0 10px #00d2ff;">
        Mika Ke7la : <span id="score" style="color:#f1c40f;">0</span>
    </div>
    
    <canvas id="snakeGame" style="border:3px solid #00d2ff; border-radius:15px; background:#24344d; touch-action:none; width: 95%; max-width: 350px; aspect-ratio: 1/1;"></canvas>
    
    <div style="margin-top:20px; display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; width:210px; margin-left:auto; margin-right:auto;">
        <div></div>
        <button onclick="changeDir('UP')" style="height:65px; border-radius:15px; background:#0f3460; color:white; border:2px solid #00d2ff; font-size:24px;">⬆️</button>
        <div></div>
        
        <button onclick="changeDir('LEFT')" style="height:65px; border-radius:15px; background:#0f3460; color:white; border:2px solid #00d2ff; font-size:24px;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="height:65px; border-radius:15px; background:#0f3460; color:white; border:2px solid #00d2ff; font-size:24px;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="height:65px; border-radius:15px; background:#0f3460; color:white; border:2px solid #00d2ff; font-size:24px;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
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
        // Effet de lumière autour du sachet pour le rendre visible
        ctx.shadowBlur = 15;
        ctx.shadowColor = "white";
        
        ctx.fillStyle = "#000000";
        ctx.beginPath();
        // Le corps du sachet
        ctx.roundRect(x + 3, y + 5, 14, 12, 3);
        ctx.fill();
        
        // Le noeud du sachet
        ctx.beginPath();
        ctx.moveTo(x+10, y+5);
        ctx.lineTo(x+5, y+1);
        ctx.lineTo(x+15, y+1);
        ctx.fill();

        ctx.shadowBlur = 0; // On enlève l'effet pour le reste
    }

    function draw() {
        ctx.fillStyle = "#24344d"; // Fond bleu-gris pour contraste
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
            clearInterval(game);
            alert("Khrat 3lik papaya !");
            location.reload();
        }

        snake.unshift(newHead);
    }

    function collision(head, array) {
        for(let i = 0; i < array.length; i++) {
            if(head.x == array[i].x && head.y == array[i].y) return true;
        }
        return false;
    }

    // Vitesse ralentie (150ms au lieu de 110ms)
    let game = setInterval(draw, 150);
</script>
"""

components.html(game_code, height=800)
