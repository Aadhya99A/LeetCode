bool isPowerOfTwo(int n) {
    if (n <= 0){
        return false;
    }
    else if (n == 1){
        return true;
    }
    else if (n%2 == 1){ // if odd number
        return false;
    }
    else{
        return isPowerOfTwo(n/2);
    }
}
