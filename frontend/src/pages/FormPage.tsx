import { Button, Col, Container, Row } from 'react-bootstrap';
import FormQuestion from '../components/FormQuestion';
import { FormQuestionType, FormQuestionObject } from '../data/FormQuestionType';
import { useLocation, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { apiGet } from '../utils/api';
export const FormPage = () => {

  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const [visibleIndex, setVisibleIndex] = useState(0);
  const location = useLocation();
  const [formData, setFormData] = useState(Array<FormQuestionObject>());

  const changeForm = () => {

    setIsLoading(true);

    // pseudo delay
    setTimeout(() => {
      setIsLoading(false);
      navigate('/form');
    }, 1000);
  }

  async function fetchData() {
    const data = await apiGet('start')
    setFormData(data.data)
    console.log(data)
  }

  useEffect(() => {
    setVisibleIndex(0);
    fetchData();
    
  },[location])
  return (
    <Container key={location.key}>
      <FormQuestion 
        id={0} 
        question="Formular Introductiv" 
        isRequired={false} 
        type={FormQuestionType.NONE}
        appear={true}
      />
      <Row>
      {formData.map((value, index) => {
        const onTrigger = () => {
          // Enable the next object in the list by updating its isRequired state
          setVisibleIndex(index + 1);
        };

        return (
          <Col md={3} key={index}>
            <FormQuestion
              id={index} 
              type={FormQuestionType.SHORT_ANSWER}
              description={value.text} 
              isRequired={index === 0} // Only the first question is required initially
              is_critical={value.is_critical} 
              appear={index <= visibleIndex}
              onTrigger={onTrigger} // Pass the onTrigger function
              data-testid={`question-${index}`} // Add a test ID for easier access
            />
          </Col>
        );
      })}
      </Row>
      <Button variant="dark" className="mt-4" onClick={changeForm} disabled={isLoading || visibleIndex < formData.length}>
                    {isLoading ? 'Loading...' : 'Continue'}
      </Button>
    </Container>

  );
}
