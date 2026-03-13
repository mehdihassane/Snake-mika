import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mika K7la Snake", layout="centered")

st.title("🐍 Snake : Edition Mika K7la")
st.write("Aide le serpent à ramasser les sachets noirs !")

# Le jeu est codé en JS pour une réactivité parfaite sur mobile (iOS/Android)
game_code = """
<div id="game-container" style="text-align:center;">
    <div style="font-size:24px; color:white; background:#333; padding:10px; border-radius:10px; margin-bottom:10px;">
        Sachets (Mika K7la) : <span id="score">0</span>
    </div>
    <canvas id="snakeGame" width="300" height="300" style="border:5px solid #555; background:#000; touch-action:none;"></canvas>
    <br><br>
    <div id="controls" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; width:200px; margin:auto;">
        <div></div><button onclick="changeDir('UP')" style="padding:20px;">⬆️</button><div></div>
        <button onclick="changeDir('LEFT')" style="padding:20px;">⬅️</button>
        <button onclick="changeDir('DOWN')" style="padding:20px;">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="padding:20px;">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");
    const box = 20;
    let score = 0;
    let snake = [{x: 9 * box, y: 10 * box}];
    let food = {x: Math.floor(Math.random()*15)*box, y: Math.floor(Math.random()*15)*box};
    let d;

    function changeDir(dir) {
        if(dir == "UP" && d != "DOWN") d = "UP";
        if(dir == "DOWN" && d != "UP") d = "DOWN";
        if(dir == "LEFT" && d != "RIGHT") d = "LEFT";
        if(dir == "RIGHT" && d != "LEFT") d = "RIGHT";
    }

    function draw() {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let i = 0; i < snake.length; i++) {
            ctx.fillStyle = (i == 0) ? "#2ecc71" : "#27ae60"; // Vert pour le serpent
            ctx.fillRect(snake[i].x, snake[i].y, box, box);
        }

        // Dessin de la Mika K7la (Sachet Noir)
        ctx.fillStyle = "#1a1a1a";
        ctx.fillRect(food.x, food.y, box, box);
        ctx.strokeStyle = "white";
        ctx.strokeRect(food.x, food.y, box, box);

        let snakeX = snake[0].x;
        let snakeY = snake[0].y;

        if( d == "LEFT") snakeX -= box;
        if( d == "UP") snakeY -= box;
        if( d == "RIGHT") snakeX += box;
        if( d == "DOWN") snakeY += box;

        if(snakeX == food.x && snakeY == food.y) {
            score++;
            scoreElement.innerHTML = score;
            food = {x: Math.floor(Math.random()*15)*box, y: Math.floor(Math.random()*15)*box};
        } else {
            snake.pop();
        }

        let newHead = {x: snakeX, y: snakeY};

        if(snakeX < 0 || snakeX >= canvas.width || snakeY < 0 || snakeY >= canvas.height || collision(newHead, snake)) {
            clearInterval(game);
            alert("Game Over ! Score : " + score + " Mika K7la");
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

    let game = setInterval(draw, 150);
</script>
"""

components.html(game_code, height=600)
