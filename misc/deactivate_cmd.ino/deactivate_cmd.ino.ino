// This function deactivates the modifications made to do cmd over USB.
void setup() {
system("rm /sketch/sketch.elf");
system("cp /etc/inittab.bak /etc/inittab");
system("kill -SIGHUP 1");

}

void loop() {
  // put your main code here, to run repeatedly:

}
