var waveObj = function(){
	this.x = [];
	this.y = [];
	this.alive = [];//free or using  true:is using;false:free
	this.r = [];//special efficient circle's radius
}
waveObj.prototype.num = 10;
waveObj.prototype.init = function(){
	for(var i = 0;i < this.num;i++){
		this.alive[i] = false;
		this.r[i] = 0;
	}
}
waveObj.prototype.draw = function(){
	ctx1.save();
	ctx1.lineWidth = 2;
	ctx1.shadowBlur = 10;
	ctx1.shadowColor = "white";
	for(var i = 0;i < this.num;i++){
		if(this.alive[i]){//if is using, then draw circle 
			//draw
			this.r[i] += deltaTime * 0.05;
			if(this.r[i] > 50){
				this.alive[i] = false;
				break;
			}
			var alpha = 1 - this.r[i] / 50;
			ctx1.beginPath();
			ctx1.arc(this.x[i],this.y[i], this.r[i], 0 * Math.PI, 2 * Math.PI);
			ctx1.closePath();
			ctx1.strokeStyle = "rgba(255,255,255," + alpha + ")";
			ctx1.stroke();
		}
	}
	ctx1.restore();
}
waveObj.prototype.born = function(x,y){
	for(var i = 0;i < this.num;i++){
		if(!this.alive[i]){//born
			this.alive[i] = true;
			this.x[i] = x;
			this.y[i] = y;
			this.r[i] = 10;
			return;
		}
	}
}
