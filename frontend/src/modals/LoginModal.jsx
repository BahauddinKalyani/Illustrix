import React from 'react';
import { Button, Modal } from 'antd';
import { Checkbox, Form, Input } from 'antd';

class LoginModal extends React.Component {

  login() {
    this.props.updateLoginModal(false)
  }
  render() {
    return (
    <>
      <Modal
        title={this.props.title}
        style={{ top: 120 }}
        open={this.props.login_modal_open}
        // onOk={() => props.updateState(false)}
        onCancel={() => this.props.updateLoginModal(false)}
        width={500}
        footer={null}
      >
        <Form
            name="basic"
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 16 }}
            style={{ maxWidth: 600 }}
            initialValues={{ remember: true }}
            // onFinish={onFinish}
            // onFinishFailed={onFinishFailed}
            autoComplete="off"
        >
            <Form.Item
                label="Username"
                name="username"
                rules={[{ required: true, message: 'Please input your username!' }]}
            >
                <Input />
            </Form.Item>

            <Form.Item
                label="Password"
                name="password"
                rules={[{ required: true, message: 'Please input your password!' }]}
            >
                <Input.Password />
            </Form.Item>

            <Form.Item name="remember" valuePropName="checked" wrapperCol={{ offset: 8, span: 16 }}>
                <Checkbox>Remember me</Checkbox>
            </Form.Item>

            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                <Button type="primary" htmlType="submit" onSubmit={()=> this.login}>
                    Login
                </Button>
            </Form.Item>
        </Form>
      </Modal>
    </>
  )};
};

export default LoginModal;