# Importing the orginal text to a string in R
# In order to use Vishaal's code in it's present form one must import and store the file as god_message

god_message

# Creating an extra object for redundancy

god2 <- god_message

# Converting the A,C,T,G to binary 1 and 0

god3 <- gsub('A','0',god2)

god3 <- gsub('C','0',god3)

god3 <- gsub('T','1',god3)

god3 <- gsub('G','1',god3)

god4 <- gsub('\n', '' , god3)

# creating frame shifted versions, 

god41 <- substr(god4, 2, 200000)

god42 <- substr(god4, 3, 200000)

god43 <- substr(god4, 4, 200000)

god44 <- substr(god4, 5, 200000)

god45 <- substr(god4, 6, 200000)

god46 <- substr(god4, 7, 200000)

god47 <- substr(god4, 8, 200000)

# choosing the correct fraem shifted version... I did this by running each one to be honest and then visually checking the output text file... can make a function to check based on dictionary words.. but anywho

godx <- god43 


# Converting to a vector with strings of length 8, allowing for subsequent conversion by a ascii lookup function

god5 <- substring(godx, seq(1,nchar(godx),8), seq(8,nchar(godx),8))

# The binary to ascii function

decode_god <- function(x){
    if (x == '01100001') {
      x <- 'a'  
}
else if (x == '01000001'){
      x <- 'A'
    }

else if (x == '01100010'){
  x <- 'b'
}

else if (x == '01000010'){
  x <- 'B'
}

else if (x == '01100011'){
  x <- 'c'
}

else if (x == '01000011'){
  x <- 'C'
}

else if (x == '01100100'){
  x <- 'd'
}

else if (x == '01000100'){
  x <- 'D'
}

else if (x == '01100101'){
  x <- 'e'
}

else if (x == '01000101'){
  x <- 'E'
}

else if (x == '01100110'){
  x <- 'f'
}

else if (x == '01000110'){
  x <- 'F'
}

else if (x == '01100111'){
  x <- 'g'
}

else if (x == '01000111'){
  x <- 'G'
}

else if (x == '01101000'){
  x <- 'h'
}

else if (x == '01001000'){
  x <- 'H'
}

else if (x == '01101001'){
  x <- 'i'
}

else if (x == '01001001'){
  x <- 'I'
}

else if (x == '01101010'){
  x <- 'j'
}

else if (x == '01001010'){
  x <- 'J'
}

else if (x == '01101011'){
  x <- 'k'
}

else if (x == '01001011'){
  x <- 'K'
}

else if (x == '01101100'){
  x <- 'l'
}

else if (x == '01001100'){
  x <- 'L'
}

else if (x == '01101101'){
  x <- 'm'
}

else if (x == '01001101'){
  x <- 'M'
}

else if (x == '01101110'){
  x <- 'n'
}

else if (x == '01001110'){
  x <- 'N'
}

else if (x == '01101111'){
  x <- 'o'
}

else if (x == '01001111'){
  x <- 'O'
}

else if (x == '01110000'){
  x <- 'p'
}

else if (x == '01010000'){
  x <- 'P'
}

else if (x == '01110001'){
  x <- 'q'
}

else if (x == '01010001'){
  x <- 'Q'
}

else if (x == '01110010'){
  x <- 'r'
}

else if (x == '01010010'){
  x <- 'R'
}

else if (x == '01110011'){
  x <- 's'
}

else if (x == '01010011'){
  x <- 'S'
}

else if (x == '01110100'){
  x <- 't'
}

else if (x == '01010100'){
  x <- 'T'
}

else if (x == '01110101'){
  x <- 'u'
}

else if (x == '01010101'){
  x <- 'U'
}

else if (x == '01110110'){
  x <- 'v'
}

else if (x == '01010110'){
  x <- 'V'
}

else if (x == '01110111'){
  x <- 'w'
}

else if (x == '01010111'){
  x <- 'W'
}

else if (x == '01111000'){
  x <- 'x'
}

else if (x == '01011000'){
  x <- 'X'
}

else if (x == '01111001'){
  x <- 'y'
}

else if (x == '01011001'){
  x <- 'Y'
}

else if (x == '01111010'){
  x <- 'z'
}

else if (x == '01011010'){
  x <- 'Z'
}
  
  else if (x == '00100000'){
    x <- ' '
  }  

else x<- '-'
}

# applying the function to the data

god_char <- sapply(god5, decode_god, simplify = TRUE)

# converting to a continuous single string (from the vector)

god_merge <- paste(god_char, sep = '', collapse = '')

# getting rid of the non alphabet and space characters

god_letter <- gsub('-', '', god_merge)

# quick visualisation of the output

god_letter

# writng the output to a text file

write.csv(god_letter, file = 'god_out.txt')
