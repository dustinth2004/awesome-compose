package main

import (
	"fmt"
	"log"
	"net/http"
)

// handler is a simple HTTP handler that writes a "Hello from Docker!" message.
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.URL.RawQuery)
	fmt.Fprintf(w, `
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
/"""""""""""""""""\___/ ===
{                       /  ===-
\______ O           __/
 \    \         __/
  \____\_______/

	
Hello from Docker!

`)
}

// main is the entry point of the application.
// It registers the handler for the root path and starts the HTTP server.
func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":80", nil))
}
