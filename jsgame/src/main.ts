import { Canvas } from "../lib/Canvas";
import { Keyboard } from "../lib/Keyboard";
import { Mouse } from "../lib/Mouse";
import { Character } from "./Character";
import { Ground } from "./Ground";

var canvas = new Canvas();
var keyboard = new Keyboard();
keyboard.initialize();
var mouse = new Mouse();
mouse.initialize()


var player = new Character(0, 0, 50, 50, 5, 'red')
var ground = new Ground(0, -350, 1000, 20, 'green')
var ground2 = new Ground(200, -180, 250, 30, 'green')


function frameLoop() {
  canvas.erase();
  canvas.drawAxes();


  player.move(keyboard)
  player.update()
  player.gravity(ground)
  
  player.render(canvas)
  ground.render(canvas)
  ground2.render(canvas)

  // canvas.fillRectangle(x, y, w, h, color);

  // if (player.y >= -225) { 
  //   player.y -=1
  // }
  // if (player.y <= -225){
  //   if (keyboard.keys(' ')) 
  // {player.y +=100 
  // }}


  // if (A) {
  //   if (B) {

  //   }
  // }
  // if (A && B) {

  // }
  // if (keyboard.keys("q")) {
  //   player.speed = player.speed *=0.8
  // }
  // if (keyboard.keys("e")) {
  //   player.speed = player.speed *=1.2
  // }

  // if (keyboard.keys("Shift")) {
  //   player.speed = 100
  // }
  
  // if (keyboard.keys("d")) {
  //   player.x += player.speed
  // }
  // if (keyboard.keys("a")) {
  //   player.x -= player.speed
  // }


  requestAnimationFrame(frameLoop);
}

frameLoop();
