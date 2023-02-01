// ----------------------------------------------------------------------------------------------
// Ball object, inherits from Sprite.
// ----------------------------------------------------------------------------------------------
var Ball = function (name, painter, behaviours, table, colour, initCx, initCy, r) {

    // Call the Sprite (i.e. base-object) constructor.
    Sprite.call(this, name, painter, behaviours);

    // Additional Ball-specific properties. Distances are in metres, and angles are in degrees.
    this.table = table;
    this.colour = colour;
    this.cx = initCx;
    this.cy = initCy;
    this.r = r;
    this.angle = 0;

    // Additional properties to help us manage game strategy.
    this.isColliding = [];
    this.isPocketed = false;

    return this;
};

// Ball inherits all the methods from Sprite.
Ball.prototype = new Sprite();

// Additional Ball method, to re-spot a ball after it has been pocketed.
Ball.prototype.respot = function (cx, cy) {
    this.cx = cx;
    this.cy = cy;
    this.isVisible = true;
    this.isPocketed = false;
};

