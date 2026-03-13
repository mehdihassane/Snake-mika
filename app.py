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

st.markdown("<h1 style='text-align: center; color: #00d2ff; font-family: sans-serif; text-shadow: 2px 2px #f1c40f;'>🐍 Snake Bello Chico</h1>", unsafe_allow_html=True)

game_code = """
<div id="game-container" style="position:relative; text-align:center; font-family: sans-serif; background: #1a1a2e; padding: 15px; border-radius: 20px;">
    
    <div id="game-over-screen" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(26, 26, 46, 0.95); z-index:10; border-radius:20px; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:#ff4b2b; font-size:40px; text-shadow: 0 0 20px #ff4b2b;">GAME OVER</h1>
        <p style="color:white; font-size:24px; font-weight:bold; margin-bottom:20px;">Khrat 3lik papaya !</p>
        <button onclick="location.reload()" style="padding:15px 30px; font-size:20px; background:#2ecc71; color:white; border:none; border-radius:50px; box-shadow: 0 5px #27ae60;">REJOUER 🔄</button>
    </div>

    <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
        <div style="font-size:22px; color:#f1c40f; font-weight:bold;">Mika : <span id="score">0</span></div>
        <div id="skin-label" style="font-size:18px; color:#00d2ff; font-weight:bold; border:1px solid #00d2ff; padding:2px 10px; border-radius:10px;">Skin: Vert</div>
    </div>
    
    <canvas id="snakeGame" style="border:4px solid #f1c40f; border-radius:15px; background:#24344d; touch-action:none; width: 95%; max-width: 350px; aspect-ratio: 1/1;"></canvas>
    
    <div style="margin-top:15px; display:flex; justify-content:center; gap:10px;">
        <button onclick="setSkin('#2ecc71', '#27ae60', 'Vert')" style="background:#27ae60; color:white; border:none; padding:8px; border-radius:5px;">Skin Vert</button>
        <button onclick="setSkin('#00d2ff', '#3a86ff', 'Bleu')" style="background:#3a86ff; color:white; border:none; padding:8px; border-radius:5px;">Skin Bleu</button>
    </div>

    <div style="margin-top:20px; display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; width:210px; margin-left:auto; margin-right:auto;">
        <div></div><button onclick="changeDir('UP')" style="height:65px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px;">⬆️</button><div></div>
        <button onclick="changeDir('LEFT')" style="height:65px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="height:65px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="height:65px; border-radius:18px; background:#0f3460; color:white; border:2px solid #f1c40f; font-size:26px;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");
    const skinLabel = document.getElementById("skin-label");
    canvas.width = 400; canvas.height = 400;
    
    const box = 20;
    let score = 0;
    let snake = [{x: 10 * box, y: 10 * box}, {x: 9 * box, y: 10 * box}];
    let food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
    let d = "RIGHT";
    
    // Variables de Skin
    let headColor = "#2ecc71";
    let bodyColor = "#27ae60";

    function setSkin(head, body, name) {
        headColor = head;
        bodyColor = body;
        skinLabel.innerHTML = "Skin: " + name;
    }

    function changeDir(dir) {
        if(dir == "UP" && d != "DOWN") d = "UP";
        if(dir == "DOWN" && d != "UP") d = "DOWN";
        if(dir == "LEFT" && d != "RIGHT") d = "LEFT";
        if(dir == "RIGHT" && d != "LEFT") d = "RIGHT";
    }

    function drawMika(x, y) {
        // Petit effet de clignotement (pulsation)
        let pulse = 10 + Math.sin(Date.now() / 100) * 5;
        ctx.shadowBlur = pulse;
        ctx.shadowColor = "white";
        
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
            ctx.fillStyle = (i == 0) ? headColor : bodyColor;
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

    let game = setInterval(draw, 150);
</script>
"""

components.html(game_code, height=880)
