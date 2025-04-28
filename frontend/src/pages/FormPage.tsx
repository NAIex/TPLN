import { Button, Col, Container, Row } from 'react-bootstrap';
import FormQuestion from '../components/FormQuestion';
import { FormQuestionType } from '../data/FormQuestionType';
import { useLocation, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
export const FormPage = () => {

  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const [visibleIndex, setVisibleIndex] = useState(0);
  const location = useLocation();

  const changeForm = () => {

    setIsLoading(true);

    // pseudo delay
    setTimeout(() => {
      setIsLoading(false);
      navigate('/form');
    }, 1000);
  }

  useEffect(() => {
    setVisibleIndex(0);
  },[location])
  return (
    <Container key={location.key}>
      <FormQuestion 
        id={0} 
        question="În ultimele două săptămâni..." 
        isRequired={false} 
        type={FormQuestionType.NONE}
        appear={true}
      />
      <Row>
      {Array.from({ length: 10 }).map((_, index) => {
        const onTrigger = () => {
          // Enable the next object in the list by updating its isRequired state
          setVisibleIndex(index + 1);
        };

        return (
          <Col md={3} key={index}>
            <FormQuestion
              id={index} 
              type={FormQuestionType.SHORT_ANSWER}
              description={`... v-ați simțit trist(ă) sau deprimat(ă)?`} 
              isRequired={index === 0} // Only the first question is required initially
              appear={index <= visibleIndex}
              onTrigger={onTrigger} // Pass the onTrigger function
              data-testid={`question-${index}`} // Add a test ID for easier access
            />
          </Col>
        );
      })}
      </Row>
      <Button variant="dark" className="mt-4" onClick={changeForm} disabled={isLoading || visibleIndex < 10}>
                    {isLoading ? 'Loading...' : 'Continue'}
      </Button>
    </Container>

  );
}
