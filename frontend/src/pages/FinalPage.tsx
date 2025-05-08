import { Container, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from 'react';
import { useLocalStorage } from 'react-use';
import { getDiagnosis } from '../utils/finalPageFunctions';

export const FinalPage = () => {

    const [totalFormAnswer, setTotalFormAnswer] = useLocalStorage<{}>('total-form-answer', {})
    const [descriptionData, setDescriptionData] = useLocalStorage<string>('description-data', '')
    
    const [diagnosis, setDiagnosis] = useState('')

    async function displayDiagnosis(){
        const answer = await getDiagnosis(descriptionData, totalFormAnswer);

        setDiagnosis(answer)
    }

    useEffect(() => {
        displayDiagnosis();
    },[])

  return (
    <Container className="mt-5">
      <h1 className="text-center">Your Recommendation</h1>

      <Card className="mt-4">
        <Card.Body>
          <Card.Text>
            {diagnosis}
          </Card.Text>
        </Card.Body>
      </Card>

      <Alert variant="warning" className="mt-4">
        This is not a diagnosis; it is just a simple recommendation. Please note that the AI can make mistakes, and you should seek professional help to determine whether you have an issue.
      </Alert>
    </Container>
  );
};
