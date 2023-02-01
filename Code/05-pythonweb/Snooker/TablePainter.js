// ----------------------------------------------------------------------------------------------
// TablePainter object.
// ----------------------------------------------------------------------------------------------
var TablePainter = function () {
    return this;
};

TablePainter.prototype = {

    // Paint everything for the snooker table.
    doPaint: function (table, ctx) {
        
        // Calculate the pixels per metre.
        var ppm = ctx.canvas.width / table.width;

        this.paintTable(table, ctx, ppm);
        this.paintPockets(table, ctx, ppm);
        this.paintBaulk(table, ctx, ppm);
        this.paintSpots(table, ctx, ppm);
    },

    // Paint the green baize for the table.
    paintTable: function (table, ctx, ppm) {

        ctx.save();

        ctx.fillStyle = 'green';
        ctx.fillRect(0, 0, table.width * ppm, table.height * ppm);

        ctx.restore();
    },

    // Paint 6 pockets.
    paintPockets: function (table, ctx, ppm) {

        ctx.save();

        // Clip to the table rectangle, to prevent pockets from overlapping table edge.
        ctx.beginPath();
        ctx.rect(0, 0, table.width * ppm, table.height * ppm);
        ctx.clip();

        // Paint all the pockets.
        ctx.fillStyle = '#632a01';
        for (var p = 0; p < table.pockets.length; p++) {
            ctx.beginPath();
            ctx.arc(table.pockets[p].cx * ppm,
                    table.pockets[p].cy * ppm,
                    table.rPocket * ppm,
                    0, 2 * Math.PI, false);
            ctx.fill();
        }

        ctx.restore();
    },

    // Paint the baulk (i.e. the white line and D at the top of the table).
    paintBaulk: function (table, ctx, ppm) {

        ctx.save();

        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;

        // Paint the baulk line.
        ctx.beginPath();
        ctx.moveTo(table.xBaulk * ppm, 0);
        ctx.lineTo(table.xBaulk * ppm, table.height * ppm);
        ctx.stroke();

        // Paint the baulk D.
        ctx.beginPath();
        ctx.arc(table.xBaulk * ppm,
                (table.height / 2) * ppm,
                table.rBaulk * ppm,
                Math.PI / 2,
                3 * Math.PI / 2,
                false);
        ctx.stroke();

        ctx.restore();
    },

    // Paint spots for all the colour balls.
    paintSpots: function (table, ctx, ppm) {

        ctx.save();

        ctx.fillStyle = 'yellow';
        ctx.lineWidth = 1;

        for (var key in table.spots) {

            // Don't paint a spot for the cue ball (this 'spot' object is just to remember where to put the cue ball).
            if (key == 'cue')
                continue;

            ctx.beginPath();
            var spot = table.spots[key];
            ctx.arc(spot.cx * ppm,
                    spot.cy * ppm,
                    3,
                    0,
                    2 * Math.PI,
                    false);
            ctx.fill();
        }

        ctx.restore();
    }
};

