// ----------------------------------------------------------------------------------------------
// Brick object, inherits from Sprite.
// ----------------------------------------------------------------------------------------------
var Brick = function (name, painter, behaviours, row, column, width, height) {

    // Call the Sprite (i.e. base-object) constructor.
    Sprite.call(this, name, painter, behaviours);

    // Additional Brick-specific properties.
    this.row = row;
    this.column = column;
    this.width = width;
    this.height = height;
    this.offsetRows = 2;

    return this;
};

// Brick inherits all the methods from Sprite.
Brick.prototype = new Sprite();

// Additional Brick-specific methods.
Brick.prototype.left = function() {
    return this.column * this.width;
};

Brick.prototype.right = function() {
    return (this.column + 1) * this.width;
};

Brick.prototype.top = function () {
    return (this.row + this.offsetRows) * this.height;
};

Brick.prototype.bottom = function () {
    return (this.row + this.offsetRows + 1) * this.height;
};


// ----------------------------------------------------------------------------------------------
// BrickPainter object.
// ----------------------------------------------------------------------------------------------
var BrickPainter = function () {
    return this;
};

BrickPainter.prototype = {

    doPaint: function (brick, ctx) {
        ctx.save();
        ctx.beginPath();
        
        // Choose a colour for the brick, based on its row.
        var effectiveRow = brick.row + brick.offsetRows;
        if (effectiveRow < 5) {
            ctx.fillStyle = 'skyblue';
        }
        else if (effectiveRow < 10) {
            ctx.fillStyle = 'blue';
        }
        else if (effectiveRow < 15) {
            ctx.fillStyle = 'darkblue';
        }
        else if (effectiveRow < 20) {
            ctx.fillStyle = 'orange';
        }
        else if (effectiveRow < 25) {
            ctx.fillStyle = 'red';
        }
        else {
            ctx.fillStyle = 'purple';
        }

        // Translate the coordinate system ready for this brick, and then draw it.
        ctx.translate(brick.left(), brick.top());
        ctx.fillRect(1, -1, brick.width - 2, brick.height - 2);

        ctx.restore();
    }
};

// ----------------------------------------------------------------------------------------------
// BrickBehaviour object.
// ----------------------------------------------------------------------------------------------
var BrickBehaviour = function (tScrollInterval) {
    this.tScrollInterval = tScrollInterval;
    this.tLastScroll = undefined;
    return this;
};


BrickBehaviour.prototype = {

    doBehaviour: function (brick, tNow, ctx) {

        // After the specified time interval has elapsed (as per this.tScrollInterval), scroll the brick 1 row downwards.
        if (!this.tLastScroll) {
            this.tLastScroll = tNow;
        }
        else if (tNow - this.tLastScroll > this.tScrollInterval) {
            this.tLastScroll = tNow;
            brick.offsetRows++;
        }
    }
};
