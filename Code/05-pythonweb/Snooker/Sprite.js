// ----------------------------------------------------------------------------------------------
// Basic Sprite object, defines core Sprite framework (i.e. hooks into a painter and behaviours).
// ----------------------------------------------------------------------------------------------
var Sprite = function (name, painter, behaviours) {

    this.name = name;
    this.painter = painter;
    this.behaviours = behaviours;

    this.isVisible = true;
    this.v = 0;

    return this;
};


Sprite.prototype = {
    
    paint: function (ctx) {
        if (this.painter && this.isVisible) {
            this.painter.doPaint(this, ctx);      
        }
    },

    update: function (tNow, ctx) {
        if (this.v != 0) {
            for (var i = this.behaviours.length - 1; i >= 0; i--) {
                this.behaviours[i].doBehaviour(this, tNow, ctx);
            }
        }
    }
};
