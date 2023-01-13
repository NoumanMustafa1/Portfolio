import Navbar from "./Components/navbar";
import { Route,Router } from "react-router-dom";

function App() {
  return (
    <Router>
    <Route>
       <Navbar />
    </Route>
    </Router>
    
  );
}

export default App;
