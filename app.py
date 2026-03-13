import streamlit as st
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mika K7la Ultra HD", layout="centered")

# Interface simplifiée et propre
st.markdown("<h1 style='text-align: center; color: #2ecc71;'>🐍 Snake Pro Edition</h1>", unsafe_allow_html=True)

game_code = """
<div id="game-container" style="text-align:center; font-family: sans-serif;">
    <div style="font-size:30px; color:#f1c40f; font-weight:bold; margin-bottom:10px;">
        Mika K7la : <span id="score">0</span>
    </div>
    <canvas id="snakeGame" width="340" height="340" style="border:8px solid #34495e; border-radius:15px; background:#121212; touch-action:none;"></canvas>
    
    <div style="margin-top:20px; display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; width:210px; margin-left:auto; margin-right:auto;">
        <div></div><button onclick="changeDir('UP')" style="padding:25px; border-radius:12px; background:#34495e; color:white; border:none; font-size:20px;">⬆️</button><div></div>
        <button onclick="changeDir('LEFT')" style="padding:25px; border-radius:12px; background:#34495e; color:white; border:none; font-size:20px;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="padding:25px; border-radius:12px; background:#34495e; color:white; border:none; font-size:20px;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="padding:25px; border-radius:12px; background:#34495e; color:white; border:none; font-size:20px;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");
    const box = 20;
    let score = 0;
    let snake = [{x: 8 * box, y: 8 * box}, {x: 7 * box, y: 8 * box}];
    let food = {x: Math.floor(Math.random()*15 + 1)*box, y: Math.floor(Math.random()*15 + 1)*box};
    let d = "RIGHT";

    function changeDir(dir) {
        if(dir == "UP" && d != "DOWN") d = "UP";
        if(dir == "DOWN" && d != "UP") d = "DOWN";
        if(dir == "LEFT" && d != "RIGHT") d = "LEFT";
        if(dir == "RIGHT" && d != "LEFT") d = "RIGHT";
    }

    // Dessiner le sachet noir (Mika K7la)
    function drawMika(x, y) {
        ctx.fillStyle = "#000000";
        // Corps du sachet
        ctx.beginPath();
        ctx.roundRect(x + 4, y + 6, 12, 12, 3);
        ctx.fill();
        // Le petit nœud du sachet en haut
        ctx.beginPath();
        ctx.moveTo(x + 10, y + 6);
        ctx.lineTo(x + 6, y + 2);
        ctx.lineTo(x + 14, y + 2);
        ctx.closePath();
        ctx.fill();
        // Petit reflet pour le plastique
        ctx.strokeStyle = "#444";
        ctx.strokeRect(x + 6, y + 8, 3, 3);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Dessiner le Serpent
        for(let i = 0; i < snake.length; i++) {
            ctx.fillStyle = (i == 0) ? "#2ecc71" : "#27ae60";
            ctx.beginPath();
            ctx.arc(snake[i].x + box/2, snake[i].y + box/2, box/2 - 2, 0, 2 * Math.PI);
            ctx.fill();
            
            // Yeux sur la tête
            if(i == 0) {
                ctx.fillStyle = "white";
                ctx.beginPath(); ctx.arc(snake[i].x + 6, snake[i].y + 6, 3, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 14, snake[i].y + 6, 3, 0, 2*Math.PI); ctx.fill();
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
            food = {x: Math.floor(Math.random()*15 + 1)*box, y: Math.floor(Math.random()*15 + 1)*box};
        } else {
            snake.pop();
        }

        let newHead = {x: snakeX, y: snakeY};

        if(snakeX < 0 || snakeX >= canvas.width || snakeY < 0 || snakeY >= canvas.height || collision(newHead, snake)) {
            clearInterval(game);
            alert("Perdu ! Tu as ramassé " + score + " Mika K7la");
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

    let game = setInterval(draw, 120);
</script>
"""

components.html(game_code, height=700)
    function collision(head, array) {
        for(let i = 0; i < array.length; i++) {
            if(head.x == array[i].x && head.y == array[i].y) return true;
        }
        return false;
    }

    let game = setInterval(draw, 130); // Vitesse légèrement augmentée pour plus de challenge
</script>
"""

components.html(game_code, height=750)
