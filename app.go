package main

import (
    "fmt"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Welcome to my ec2 server!")
}

func main() {
    http.HandleFunc("/", helloHandler)
    fmt.Println("Starting server on :8080...")
    http.ListenAndServe(":8080", nil)
}

