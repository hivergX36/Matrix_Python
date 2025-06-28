import re 

class Matrix:
    
    def init(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        
      
    def parsing_checknumber(self,lignes,indice,caracter:str):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != caracter and lignes[indice][compteur2] != caracter):
              while(lignes[indice][compteur2] != caracter):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def parse_data(self, text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        matrix_data = [self.parsing_checknumber(lines, i,",") for i in range(len(lines))]
        print("Matrix data:", matrix_data)
        self.rows = matrix_data[0][0]
        print("Rows:", self.rows)
        self.cols = matrix_data[0][1] 
        print("Cols:", self.cols)
        self.matrix = [[matrix_data[i][j] for j in range(0,self.cols)] for i in range(1, self.rows)]
        
    def display_matrix(self):
        print("Matrix:", self.matrix)
