/********************************************
 * Sprite object
 ********************************************/
var Sprite = function (name, painter, behaviours) {

    this.name = name;

    this.top = 0;
    this.left = 0;

    this.tStart    = undefined;
    this.velocityX = 0;
    this.velocityY = 0;
    this.isVisible = true;
    this.isRunning = true;

    this.width  = 30;
    this.height = 30;

    this.painter = painter;
    this.behaviours = behaviours;

    return this;
};


Sprite.prototype = {
    
    paint: function (ctx) {
        if (this.painter && this.isVisible) {
            this.painter.doPaint(this, ctx);      
        }
    },

    update: function (tNow, ctx) {
        if (this.isRunning) {
            for (var i = this.behaviours.length - 1; i >= 0; i--) {
                this.behaviours[i].doBehaviour(this, tNow, ctx);
                if (this.top > ctx.canvas.height || this.left > ctx.canvas.width) {
                    this.isRunning = false;
                }
            }
        }
    }
};
