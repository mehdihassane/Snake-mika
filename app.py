import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mika K7la Elite", layout="centered")

# CSS pour cacher les menus Streamlit et rendre l'app plus propre
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #1a1a2e;}
    </style>
    """, unsafe_allow_html=True)

game_code = """
<div id="game-container" style="text-align:center; font-family: 'Segoe UI', Roboto, sans-serif; background: #1a1a2e; padding: 20px; border-radius: 20px;">
    <div style="font-size:32px; color:#00d2ff; font-weight:bold; margin-bottom:15px; text-shadow: 0 0 10px #00d2ff;">
        Mika Ke7la : <span id="score" style="color:#f1c40f;">0</span>
    </div>
    
    <canvas id="snakeGame" style="border:4px solid #00d2ff; border-radius:15px; background:#16213e; touch-action:none; width: 95%; max-width: 350px; aspect-ratio: 1/1; box-shadow: 0 0 20px rgba(0, 210, 255, 0.3);"></canvas>
    
    <div style="margin-top:25px; display:grid; grid-template-columns: repeat(3, 1fr); gap:15px; width:220px; margin-left:auto; margin-right:auto;">
        <div></div>
        <button onclick="changeDir('UP')" style="height:70px; border-radius:15px; background:linear-gradient(145deg, #0f3460, #16213e); color:white; border:2px solid #00d2ff; font-size:24px; box-shadow: 4px 4px 10px #000;">⬆️</button>
        <div></div>
        
        <button onclick="changeDir('LEFT')" style="height:70px; border-radius:15px; background:linear-gradient(145deg, #0f3460, #16213e); color:white; border:2px solid #00d2ff; font-size:24px; box-shadow: 4px 4px 10px #000;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="height:70px; border-radius:15px; background:linear-gradient(145deg, #0f3460, #16213e); color:white; border:2px solid #00d2ff; font-size:24px; box-shadow: 4px 4px 10px #000;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="height:70px; border-radius:15px; background:linear-gradient(145deg, #0f3460, #16213e); color:white; border:2px solid #00d2ff; font-size:24px; box-shadow: 4px 4px 10px #000;">➡️</button>
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

    function drawGrid() {
        ctx.strokeStyle = "#1f293a";
        ctx.lineWidth = 1;
        for(let i=0; i<canvas.width; i+=box) {
            ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(0,i); ctx.lineTo(canvas.width,i); ctx.stroke();
        }
    }

    function drawMika(x, y) {
        // Ombre portée
        ctx.shadowBlur = 10;
        ctx.shadowColor = "black";
        
        // Corps du sachet (Noir Intense)
        ctx.fillStyle = "#050505";
        ctx.beginPath();
        ctx.roundRect(x + 2, y + 4, 16, 14, 4);
        ctx.fill();
        
        // Reflet plastique
        ctx.fillStyle = "rgba(255,255,255,0.2)";
        ctx.fillRect(x + 5, y + 6, 10, 2);
        
        ctx.shadowBlur = 0; // Reset ombre
    }

    function draw() {
        ctx.fillStyle = "#16213e";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        drawGrid();

        for(let i = 0; i < snake.length; i++) {
            // Effet de néon pour le serpent
            ctx.shadowBlur = (i === 0) ? 15 : 0;
            ctx.shadowColor = "#2ecc71";
            
            ctx.fillStyle = (i == 0) ? "#2ecc71" : "#27ae60";
            ctx.beginPath();
            ctx.roundRect(snake[i].x + 1, snake[i].y + 1, box - 2, box - 2, 6);
            ctx.fill();
            
            if(i == 0) { // Yeux
                ctx.fillStyle = "white";
                ctx.beginPath(); ctx.arc(snake[i].x + 6, snake[i].y + 7, 3, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 14, snake[i].y + 7, 3, 0, 2*Math.PI); ctx.fill();
            }
            ctx.shadowBlur = 0;
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

    let game = setInterval(draw, 110);
</script>
"""

components.html(game_code, height=850)
