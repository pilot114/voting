import { Injectable } from '@nestjs/common';

// Простейший пример сервиса
@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  getHelloJson(): object {
    return {
      text: 'Hello World!'
    };
  }
}
