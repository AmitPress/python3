package main
import (
	"fmt"
)
// on go it is so easy /////*/*/*
func main(){
	for i:=1; i<=5; i++{ //row
		for j:=1; j<=5; j++{ //column
			if j <= 5 - i {
				fmt.Printf("  ")
			}else{
				fmt.Printf("* ")
			}
		}
		fmt.Println("")
	}
}