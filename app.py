import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Mika K7la Snake HD", layout="centered")

# Titre avec style personnalisé
st.markdown("<h1 style='text-align: center; color: #2ecc71;'>🐍 Snake : Edition HD Mika K7la</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Aide le serpent à ramasser les sachets noirs brillants !</p>", unsafe_allow_html=True)

# Code du jeu amélioré (JS/HTML)
game_code = """
<div id="game-container" style="text-align:center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <div style="font-size:28px; color:white; background:linear-gradient(135deg, #34495e, #2c3e50); padding:15px; border-radius:15px; margin-bottom:15px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
        Sachets (Mika K7la) : <span id="score" style="font-weight: bold; color: #f1c40f;">0</span>
    </div>
    <canvas id="snakeGame" width="350" height="350" style="border:10px solid #34495e; border-radius: 10px; background:#1a1a1a; touch-action:none; box-shadow: 0 8px 12px rgba(0,0,0,0.5);"></canvas>
    <br><br>
    <div id="controls" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; width:220px; margin:auto;">
        <div></div><button onclick="changeDir('UP')" style="padding:22px; background-color: #34495e; color: white; border: none; border-radius: 10px; font-size: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">⬆️</button><div></div>
        <button onclick="changeDir('LEFT')" style="padding:22px; background-color: #34495e; color: white; border: none; border-radius: 10px; font-size: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">⬅️</button>
        <button onclick="changeDir('DOWN')" style="padding:22px; background-color: #34495e; color: white; border: none; border-radius: 10px; font-size: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">⬇️</button>
        <button onclick="changeDir('RIGHT')" style="padding:22px; background-color: #34495e; color: white; border: none; border-radius: 10px; font-size: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">➡️</button>
    </div>
</div>

<script>
    const canvas = document.getElementById("snakeGame");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");
    const box = 20;
    let score = 0;
    let snake = [{x: 9 * box, y: 10 * box}];
    let food = {x: Math.floor(Math.random()*16)*box + 20, y: Math.floor(Math.random()*16)*box + 20}; // Ajusté pour éviter les bords
    let d;

    function changeDir(dir) {
        if(dir == "UP" && d != "DOWN") d = "UP";
        if(dir == "DOWN" && d != "UP") d = "DOWN";
        if(dir == "LEFT" && d != "RIGHT") d = "LEFT";
        if(dir == "RIGHT" && d != "LEFT") d = "RIGHT";
    }

    // Fonction pour dessiner un rectangle arrondi (pour le serpent)
    function fillRoundedRect(ctx, x, y, width, height, radius) {
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + width - radius, y);
        ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
        ctx.lineTo(x + width, y + height - radius);
        ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        ctx.lineTo(x + radius, y + height);
        ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
        ctx.lineTo(x, y + radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.closePath();
        ctx.fill();
    }

    // Fonction pour dessiner la Mika K7la stylisée
    function drawMika(ctx, x, y, size) {
        ctx.fillStyle = "#000000"; // Noir profond
        fillRoundedRect(ctx, x + 2, y + 2, size - 4, size - 4, 3); // Corps du sachet
        
        ctx.fillStyle = "#ffffff"; // Reflet blanc
        ctx.beginPath();
        ctx.ellipse(x + size/2 + 3, y + size/2 - 3, size/6, size/4, Math.PI / 4, 0, 2 * Math.PI);
        ctx.fill();
        
        ctx.strokeStyle = "#ffffff"; // Contour blanc fin
        ctx.lineWidth = 1;
        ctx.strokeRect(x + 1, y + 1, size - 2, size - 2);
    }

    function draw() {
        ctx.fillStyle = "#1a1a1a"; // Fond gris très sombre
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for(let i = 0; i < snake.length; i++) {
            if (i == 0) {
                ctx.fillStyle = "#2ecc71"; // Tête vert clair
                fillRoundedRect(ctx, snake[i].x, snake[i].y, box, box, 5);
                // Yeux
                ctx.fillStyle = "white";
                ctx.beginPath(); ctx.arc(snake[i].x + box/3, snake[i].y + box/3, box/6, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 2*box/3, snake[i].y + box/3, box/6, 0, 2*Math.PI); ctx.fill();
                ctx.fillStyle = "black";
                ctx.beginPath(); ctx.arc(snake[i].x + box/3, snake[i].y + box/3, box/12, 0, 2*Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(snake[i].x + 2*box/3, snake[i].y + box/3, box/12, 0, 2*Math.PI); ctx.fill();
            } else {
                ctx.fillStyle = "#27ae60"; // Corps vert plus foncé
                fillRoundedRect(ctx, snake[i].x, snake[i].y, box, box, 3);
            }
        }

        // Dessin de la Mika K7la stylisée
        drawMika(ctx, food.x, food.y, box);

        let snakeX = snake[0].x;
        let snakeY = snake[0].y;

        if( d == "LEFT") snakeX -= box;
        if( d == "UP") snakeY -= box;
        if( d == "RIGHT") snakeX += box;
        if( d == "DOWN") snakeY += box;

        if(snakeX == food.x && snakeY == food.y) {
            score++;
            scoreElement.innerHTML = score;
            food = {x: Math.floor(Math.random()*16)*box + 20, y: Math.floor(Math.random()*16)*box + 20};
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

    let game = setInterval(draw, 130); // Vitesse légèrement augmentée pour plus de challenge
</script>
"""

components.html(game_code, height=750)
