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
    
    <div id="start-screen" style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(26, 26, 46, 0.95); z-index:20; border-radius:20px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:#f1c40f; font-size:32px; text-shadow: 2px 2px #3498db; margin-bottom: 30px;">CHOISIS TON MODE</h1>
        <button onpointerdown="startGame('solo')" style="margin-bottom: 15px; padding:15px 30px; font-size:20px; background:#2ecc71; color:white; border:none; border-radius:15px; font-weight:bold; cursor:pointer; width: 220px; box-shadow: 0 4px #27ae60;">Mode Seul 🐍</button>
        <button onpointerdown="startGame('boubalou')" style="padding:15px 30px; font-size:20px; background:#9b59b6; color:white; border:none; border-radius:15px; font-weight:bold; cursor:pointer; width: 220px; box-shadow: 0 4px #8e44ad;">VS Boubalou 😈</button>
    </div>

    <div id="game-over-screen" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(255, 0, 0, 0.9); z-index:10; border-radius:20px; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:white; font-size:40px; text-shadow: 0 0 20px black;">BOOM !</h1>
        <p id="game-over-text" style="color:white; font-size:24px; font-weight:bold; margin-bottom:20px;">Khrat 3lik papaya !</p>
        <button onpointerdown="showMenu()" style="padding:15px 30px; font-size:20px; background:white; color:red; border:none; border-radius:50px; font-weight:bold; cursor:pointer;">RETOUR MENU 🔄</button>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <div style="font-size:22px; color:#f1c40f; font-weight:bold;">Mika K7la : <span id="score" style="color:white;">0</span></div>
        <div id="mode-badge" style="font-size:16px; color:#2ecc71; font-weight:bold; border:1px solid #2ecc71; padding:2px 8px; border-radius:8px;">Mode Seul</div>
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
    
    // Variables globales
    let score;
    let snake;
    let food;
    let d;
    let changingDirection;
    let gameLoop; 
    let boubalou = [];
    let boubalouTick; 
    let currentMode = 'solo'; // Pour savoir à quoi on joue

    // --- FONCTIONS DE MENU ---
    function showMenu() {
        document.getElementById("game-over-screen").style.display = "none";
        document.getElementById("start-screen").style.display = "flex";
    }

    function startGame(mode) {
        currentMode = mode;
        
        // Réinitialisation des stats
        score = 0;
        scoreElement.innerHTML = score;
        snake = [{x: 10 * box, y: 10 * box}, {x: 9 * box, y: 10 * box}];
        food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
        d = "RIGHT";
        changingDirection = false;
        boubalouTick = 0;
        boubalou = [];

        // Gestion du badge en haut à droite
        let modeBadge = document.getElementById("mode-badge");

        if (currentMode === 'boubalou') {
            boubalou = [{x: 19 * box, y: 19 * box}, {x: 19 * box, y: 19 * box}];
            modeBadge.innerText = "VS Boubalou";
            modeBadge.style.color = "#9b59b6";
            modeBadge.style.borderColor = "#9b59b6";
        } else {
            modeBadge.innerText = "Mode Seul";
            modeBadge.style.color = "#2ecc71";
            modeBadge.style.borderColor = "#2ecc71";
        }

        // Cache les menus
        document.getElementById("start-screen").style.display = "none";
        document.getElementById("game-over-screen").style.display = "none";

        // Lance le jeu
        canvas.focus();
        if(gameLoop) clearInterval(gameLoop);
        gameLoop = setInterval(draw, 150);
    }

    function respawnBoubalou() {
        const corners = [
            {x: 0, y: 0},                 
            {x: 19 * box, y: 0},          
            {x: 0, y: 19 * box},          
            {x: 19 * box, y: 19 * box}    
        ];
        
        let validCorners = corners.filter(c => !collision(c, snake));
        if (validCorners.length === 0) validCorners = corners;

        let corner = validCorners[Math.floor(Math.random() * validCorners.length)];

        boubalou = [];
        for(let i = 0; i < snake.length; i++) {
            boubalou.push({x: corner.x, y: corner.y});
        }
    }

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

    function drawBoubalouSegment(x, y, isHead) {
        ctx.fillStyle = "#8e44ad"; 
        ctx.beginPath();
        ctx.roundRect(x + 1, y + 1, box - 2, box - 2, 8);
        ctx.fill();

        ctx.fillStyle = "#2c3e50"; 
        ctx.fillRect(x + 1, y + 12, box - 2, 7);

        if(isHead) {
            ctx.fillStyle = "white";
            ctx.font = "bold 11px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText("BOUBALOU", x + box/2, y - 4);

            ctx.fillStyle = "#333";
            ctx.fillRect(x + 1, y + 6, box - 2, 4);
            ctx.fillStyle = "white";
            ctx.beginPath(); ctx.arc(x + 10, y + 8, 5, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "#e74c3c"; 
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

    function moveBoubalou() {
        if(boubalou.length === 0) return;

        let bx = boubalou[0].x;
        let by = boubalou[0].y;
        let px = snake[0].x;
        let py = snake[0].y;

        let moves = [
            {x: bx, y: by - box}, 
            {x: bx, y: by + box}, 
            {x: bx - box, y: by}, 
            {x: bx + box, y: by}  
        ];

        let validMoves = moves.filter(m => {
            if (m.x < 0 || m.x >= canvas.width || m.y < 0 || m.y >= canvas.height) return false;
            for (let i = 0; i < boubalou.length - 1; i++) {
                if (m.x === boubalou[i].x && m.y === boubalou[i].y) return false;
            }
            return true;
        });

        if (validMoves.length === 0) return; 

        validMoves.forEach(m => {
            m.dist = Math.abs(m.x - px) + Math.abs(m.y - py);
        });

        validMoves.sort((a, b) => a.dist - b.dist);

        let chosenMove;
        if (Math.random() < 0.6) {
            chosenMove = validMoves[0];
        } else {
            chosenMove = validMoves[Math.floor(Math.random() * validMoves.length)];
        }

        boubalou.pop(); 
        boubalou.unshift({x: chosenMove.x, y: chosenMove.y}); 
    }

    function gameOver(message) {
        clearInterval(gameLoop);
        document.getElementById("game-over-text").innerText = message;
        document.getElementById("game-over-screen").style.display = "flex";
    }

    function draw() {
        changingDirection = false; 

        ctx.fillStyle = "#24344d"; 
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Boubalou ne bouge que s'il est actif
        if (currentMode === 'boubalou') {
            boubalouTick++;
            if (boubalouTick % 2 === 0) {
                moveBoubalou();
            }
        }

        let snakeX = snake[0].x;
        let snakeY = snake[0].y;
        if( d == "LEFT") snakeX -= box;
        if( d == "UP") snakeY -= box;
        if( d == "RIGHT") snakeX += box;
        if( d == "DOWN") snakeY += box;

        let newHead = {x: snakeX, y: snakeY};

        // 1. Tu meurs si tu touches un mur
        if(snakeX < 0 || snakeX >= canvas.width || snakeY < 0 || snakeY >= canvas.height) {
            gameOver("dkholti f7itt a papaya");
            return;
        }

        // 2. Tu meurs si tu touches ton propre corps
        if(collision(newHead, snake)) {
            gameOver("Khrat 3lik papaya !");
            return;
        }

        // Règles spécifiques au mode Boubalou
        if (currentMode === 'boubalou') {
            // 3. Tu meurs si TU rentres dans Boubalou
            if(collision(newHead, boubalou)) {
                gameOver("dkholti fboubalou a papaya hhhh");
                return;
            }

            // 4. Boubalou meurt s'il TE rentre dedans
            if(boubalou.length > 0 && collision(boubalou[0], snake)) {
                respawnBoubalou();
            }
        }

        // Tu manges la Mika K7la
        if(snakeX == food.x && snakeY == food.y) {
            score++;
            scoreElement.innerHTML = score;
            food = {x: Math.floor(Math.random()*18 + 1)*box, y: Math.floor(Math.random()*18 + 1)*box};
            
            // Boubalou grandit avec toi uniquement dans son mode
            if (currentMode === 'boubalou' && boubalou.length > 0) {
                boubalou.push({x: boubalou[boubalou.length - 1].x, y: boubalou[boubalou.length - 1].y});
            }
            
        } else {
            snake.pop();
        }

        snake.unshift(newHead);

        // Dessin
        for(let i = 0; i < snake.length; i++) {
            drawMinionSegment(snake[i].x, snake[i].y, i === 0);
        }

        if (currentMode === 'boubalou') {
            for(let i = 0; i < boubalou.length; i++) {
                drawBoubalouSegment(boubalou[i].x, boubalou[i].y, i === 0);
            }
        }

        drawMika(food.x, food.y);
    }

    function collision(head, array) {
        for(let i = 0; i < array.length; i++) {
            if(head.x == array[i].x && head.y == array[i].y) return true;
        }
        return false;
    }

    // Le jeu ne se lance plus tout seul ici ! Il attend que tu cliques sur le menu.
</script>
"""

components.html(game_code, height=900)
