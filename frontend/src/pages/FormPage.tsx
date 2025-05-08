import { Button, Col, Container, Row } from 'react-bootstrap';
import FormQuestion from '../components/FormQuestion';
import { FormQuestionType, FormQuestionObject } from '../data/FormQuestionType';
import { useLocation, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { apiGet } from '../utils/api';

import { useCookies } from 'react-cookie';

export const FormPage = () => {

  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const [visibleIndex, setVisibleIndex] = useState(0);
  const location = useLocation();
  const [formData, setFormData] = useState(Array<FormQuestionObject>());  

  const [cookies, setCookie] = useCookies(['userStarted','completedDataJSON',"form_names"]);

  const updateFormDataText = (index: number, value: string) => {
    const formDataCopy = [...formData];
    formDataCopy[index].text_answer = value;

    console.log(formDataCopy[index].text_answer)
    setFormData(formDataCopy);
  }  
  const updateFormDataBool = (index: number, value: boolean) => {
    const formDataCopy = [...formData];
    formDataCopy[index].bool_answer = value;

    console.log(formDataCopy[index].bool_answer)

    setFormData(formDataCopy);
  }

  const changeForm = () => {
    
    setIsLoading(true);
    
    let cookieList = cookies.form_names;
    cookieList.pop();
    setCookie('form_names',cookieList)

    if(cookieList.length == 0)
    {
      navigate('/')
      return;
    }
      
    // send data to server
    setFormCompletionDataAsCookie();
    
    // pseudo delay
    setTimeout(() => {
      setIsLoading(false);
      navigate('/form');
      window.location.reload();
    }, 1000);
  }


  const setFormCompletionDataAsCookie = () => {
    setCookie('completedDataJSON', JSON.stringify(formData.map((value) => [value.id,[value.bool_answer,value.text_answer]])), { path: '/' });
  }

  async function fetchDataBasedOnCookie(){
    const cookieList :[] = cookies.form_names
    const cookieData = cookieList[cookieList.length-1]
    if(cookieList.length === 0)
    {
      navigate('/')
      return;
    }
    if(cookieData === 'i'){
      const formData = await apiGet('start')

      const data = formData.data
      setFormData(data)
    } 
  }

  async function fetchStartData(){
    const data = await apiGet('start')
    setFormData(data.data)
    console.log(data)
  }
  async function fetchData() {
    const data = await apiGet('next-form')
    setFormData(data.data)
  }

  useEffect(() => {
    setVisibleIndex(0);
    
    /*
    if (cookies.userStarted == false) {
      setCookie('userStarted', true, { path: '/' });
      fetchStartData();
    }
    else {
      fetchData();
    }
    */
   fetchDataBasedOnCookie()

    console.log(cookies.completedDataJSON)
    
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
              question_id={value.id}
              type={FormQuestionType.SHORT_ANSWER}
              description={value.text} 
              isRequired={index === 0} // Only the first question is required initially
              is_critical={value.is_critical} 
              appear={index <= visibleIndex}
              onTrigger={onTrigger} // Pass the onTrigger function
              data-testid={`question-${index}`} // Add a test ID for easier access

              onChangeText={(text) => updateFormDataText(index, text)} // Update the text answer
              onChangeBool={(value) => updateFormDataBool(index, value)} // Update the boolean answer
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
