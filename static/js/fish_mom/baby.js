var babyObj=function(){
	this.x;
	this.y;
	this.angle;
	this.babyBody=new Image();
	
	this.babyTailTimer=0;
	this.babyTailCount=0;
	
	this.babyEyeTimer = 0;//timer control
	this.babyEyeCount = 0;//counter which frame
	this.babyEyeInterval = 1000;//close eye's time or open eye's time
	
	this.babyBodyTimer = 0;
	this.babyBodyCount = 0;
}

babyObj.prototype.init=function(){
	this.x=canWidth*0.5-50;
	this.y=canHeight*0.5+50;
	this.angle=0;
	this.babyBody.src="../../static/img/fish_mom/babyFade0.png";
}

babyObj.prototype.draw=function(){
	//let baby swim with mom
	this.x = lerpDistance(mom.x+50, this.x, 0.98);
	this.y = lerpDistance(mom.y, this.y, 0.98);
	
	//let baby rotate with mom
	var deltaY=mom.y-this.y;
	var deltaX=mom.x-this.x;
	var beta=Math.atan2(deltaY,deltaX)+Math.PI;
	//let big fish lerp to mouse's angle
	this.angle = lerpAngle(beta, this.angle, 0.6);
	
	//baby tail
	this.babyTailTimer +=deltaTime;
	if(this.babyTailTimer>50){
		this.babyTailCount = (this.babyTailCount + 1) % 8;
		this.babyTailTimer %= 50;
	}
	
	//baby eye
	this.babyEyeTimer += deltaTime;
	if(this.babyEyeTimer > this.babyEyeInterval){
		this.babyEyeCount = (this.babyEyeCount + 1) % 2;
		this.babyEyeTimer %= this.babyEyeInterval;
		if(this.babyEyeCount == 0){//if open eye
			this.babyEyeInterval = Math.random() * 1500 + 2000;
		}else{//if close eye
			this.babyEyeInterval = 200;
		}
	}
	
	//baby body
	this.babyBodyTimer += deltaTime;
	if(this.babyBodyTimer > 300){
		this.babyBodyCount = this.babyBodyCount + 1;
		this.babyBodyTimer %= 300;
		if(this.babyBodyCount > 19){
			this.babyBodyCount = 19;
			//game over
			data.gameOver = true;
		}
	}
	
	ctx1.save();
	ctx1.translate(this.x, this.y);
	ctx1.rotate(this.angle);
	
	var babyTailCount = this.babyTailCount;
	ctx1.drawImage(babyTail[babyTailCount],-babyTail[babyTailCount].width*0.5+23,-babyTail[babyTailCount].width*0.5-2);
	var babyBodyCount = this.babyBodyCount;
	ctx1.drawImage(babyBody[babyBodyCount],-babyBody[babyBodyCount].width*0.5,-babyBody[babyBodyCount].width*0.5);
	var babyEyeCount = this.babyEyeCount;
	ctx1.drawImage(babyEye[babyEyeCount], -babyEye[babyEyeCount].width*0.5, -babyEye[babyEyeCount].height*0.5+2);

	ctx1.restore();

}