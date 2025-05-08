import { Container } from "react-bootstrap"

import {Form} from 'react-bootstrap'
import { Button } from "react-bootstrap"
import { useNavigate } from "react-router-dom"
import { sendInitFeelingsText } from "../utils/startFormPageFunctions"
import { useLocalStorage } from "react-use"
import { FormStructure } from "../utils/formPageFunctions"

const StartFormPage = () => {

  const navigate = useNavigate()

  const [descriptionData, setDescriptionData] = useLocalStorage<string>('description-data', '')
  const [currentForm, setCurrentForm] = useLocalStorage<[FormStructure]>('current-form')
  const [totalFormAnswer, setTotalFormAnswer] = useLocalStorage<{}>('total-form-answer', {})

  const descriptionText =" Detaliați puțin mai mult starea dumneavoastră de spirit din ultimele 2 săptămâni.";


  async function startForm(){
    const data = await sendInitFeelingsText(descriptionData);
    setCurrentForm(data);
    setTotalFormAnswer({});

    navigate('/form')
  }

  return (
    <Container>
        <h1>Cum te mai simti in ultimul timp?</h1>
        <Form.Group className="mt-3">
            <Form.Control
             placeholder={descriptionText}  
                as="textarea" rows={10}
                style={{resize: 'none'}}
                onChange={(e) => setDescriptionData(e.target.value)}
             />
             <Form.Label className="mt-2 text-muted">
              {descriptionData.length !== 0  &&
               <div>
                  {descriptionText}
               </div>
              }
             </Form.Label>
          </Form.Group>
          <Button variant="dark" className="mt-4" onClick={startForm}>
            Continuare
          </Button>
    </Container>

    
  )
}

export default StartFormPage