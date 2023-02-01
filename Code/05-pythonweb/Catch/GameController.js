var raf = window.requestAnimationFrame       ||
          window.mozRequestAnimationFrame    ||
          window.webkitRequestAnimationFrame ||
          window.msRequestAnimationFrame     ||
          window.oRequestAnimationFrame;


var Game = function (name, canvasId) {

    var thisGame = this;

    // General properties.
    this.name = name;
    this.ctx = document.getElementById(canvasId).getContext('2d');      
    this.sprites = [];
    this.scoreTable = "ScoresTable: " + this.name;
	
    // Timing and game management properties.
    this.tStart = 0;
    this.tPrev = 0;
    this.tGame = 0;
    this.tPause = 0;
    this.tPauseTotal = 0;
    this.isPaused = false;
    this.isGameOver = false;
    this.PAUSE_TIMEOUT = 100;

    // Image-related properties.  
    this.images = {};
    this.imageUrls = [];
    this.imagesLoadedOK = 0;
    this.imagesNotLoadedOK = 0;

    // Sound-related properties.
    this.numAudiosPlaying = 0;
    this.MAX_CONCURRENT_AUDIOS = 10;

    // Keyboard-handling properties.
    this.KEY_SPACE = 32;
    this.KEY_D = 68;
    this.KEY_K = 75;
    this.KEY_P = 80;
    this.KEY_S = 83;
    this.KEY_ARROW_LEFT  = 37;
    this.KEY_ARROW_UP    = 38;
    this.KEY_ARROW_RIGHT = 39;
    this.KEY_ARROW_DOWN  = 40;
    this.keyListeners = {};

    // Keyboard and mouse event handlers.
    window.onkeypress  = function (e) { thisGame.handleKeyEvent(e); };
    window.onkeydown   = function (e) { thisGame.handleKeyEvent(e); };
    window.onmousemove = function (e) { thisGame.handleMouseMoveEvent(e); };
    window.onmousedown = function (e) { thisGame.handleMouseDownEvent(e); };

   return this;
};


Game.prototype = {

    loadImages: function (imageUrls) {

        var thisGame = this;
        this.imageUrls = imageUrls;

        for (var i = 0; i < imageUrls.length; i++) {

            var image = new Image();
            var imageUrl = imageUrls[i];
            image.src = imageUrl;
            this.images[imageUrl] = image;

            image.addEventListener('load', function (e) {
                thisGame.imagesLoadedOK++;
                thisGame.imageLoadingProgress(thisGame.getImageLoadingProgress());
            });

            image.addEventListener('error', function (e) {
                thisGame.imagesNotLoadedOK++;
                thisGame.imageLoadingProgress(thisGame.getImageLoadingProgress());
            }); 
        }
    },

    getImageLoadingProgress: function() {
        return 100 * (this.imagesLoadedOK + this.imagesNotLoadedOK) / this.imageUrls.length;
    },

    getImageByUrl: function (imageUrl) {
        return this.images[imageUrl];
    },

    start: function () {
        var thisGame = this;
        this.tStart = new Date(); 

        raf(function (tNow) {
            thisGame.draw.call(thisGame, tNow); 
        });
    },

    reset: function() {
        this.isGameOver = false;
        this.sprites = [];
    }, 

    draw: function (tNow) {
        var thisGame = this; 

        if (this.isPaused) {
            setTimeout(raf(function (tNow) {
                               thisGame.draw.call(thisGame, tNow); 
                           }, 
                           this.PAUSE_TIMEOUT));
        }
        else {
            this.tGame = tNow - this.tStart;
            this.ctx.clearRect(0, 0, this.ctx.canvas.width, this.ctx.canvas.height);

            this.preDrawFrame(tNow - this.tPauseTotal, this.tGame);  
            this.drawUnderLayer(); 

            if (!this.isGameOver) {
                for(var i=0; i < this.sprites.length; ++i) {
                    var sprite = this.sprites[i];
                    sprite.update(tNow - this.tPauseTotal, this.ctx);
                }
            }

            for (var i=0; i < this.sprites.length; ++i) {
                var sprite = this.sprites[i];
                if (sprite.isVisible) {
                    sprite.paint(this.ctx);
                }
            }

            this.drawOverLayer();  

            for (var i=0; i < this.sprites.length; ++i) {
                var sprite = this.sprites[i];
                if (!sprite.isRunning) {
                    this.onDeleteSprite(sprite);
                    this.sprites.splice(i, 1);
                }
            }

            raf(function (tNow) {
                    thisGame.draw.call(thisGame, tNow); 
                });
        }
    },

    togglePaused: function () {
        var tNow = new Date();
        this.isPaused = !this.isPaused;
        if (this.isPaused) {
            this.tPause = tNow;
        }
        else { 
            this.tPauseTotal += tNow - this.tPause;
            this.tPrev = tNow;
        }
    },

    saveScore: function(score) {
        var scoresString = localStorage[this.scoreTable];
        var scores = (scoresString) ? JSON.parse(scoresString) : [];

        for (var i = 0; i < scores.length; i++) {
            if (score.value > scores[i].value) {
                break;
            }
        }
        scores.splice(i, 0, score);
        localStorage[this.scoreTable] = JSON.stringify(scores);  
        return { scores: scores, thisScoreIndex: i };
    },

    clearScores: function() {
        localStorage[this.scoreTable] = JSON.stringify([]);  
    },

    addKeyListener: function (key, listener) {
        this.keyListeners[key] = listener;
    },

    handleKeyEvent: function (e) {
        var listener = this.keyListeners[e.keyCode];
        if (listener) {
             listener();  
        }
    },

    handleMouseMoveEvent: function (e) {},
    handleMouseDownEvent: function (e) {},

    playSound: function (audioElementid) {
        var thisGame = this;

        if (this.numAudiosPlaying < this.MAX_CONCURRENT_AUDIOS) {
            this.numAudiosPlaying++;
            var audio = document.getElementById(audioElementid);    

            audio.addEventListener('ended',  
                                    function () {  
                                        thisGame.numAudiosPlaying--; 
                                    }, 
                                    false);
            audio.play();
        }
    },

    addSprite: function (sprite) {
        this.sprites.push(sprite);
    },

    preDrawFrame:         function (tNow, tGame) {}, 
    imageLoadingProgress: function (percent) {},
    drawUnderLayer:       function () {}, 
    drawOverLayer:        function () {}, 
    onDeleteSprite:       function (sprite) {},
    postDrawFrame:        function () {}  
};

